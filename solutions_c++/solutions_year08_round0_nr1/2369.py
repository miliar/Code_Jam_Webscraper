#include <stdio.h>
#include <io.h>
#include <fcntl.h>
#include <atlstr.h>
#include <vector>
#include <algorithm>

UINT n = 0, s = 0, q = 0, switches = 0, freeEngines = 0, currentEngine = (UINT) -1;
std::vector<CString> engines, queries;
std::vector<bool> usedEngines;

int _tmain()
{
	int res = _ftscanf_s(stdin, _T("%u"), &n);
	if ((!res) || (res == EOF)) 
		return -1;

	for (UINT nc = 0; nc < n; ++nc)
	{
		res = _ftscanf_s(stdin, _T("%u\n"), &s);
		if ((!res) || (res == EOF)) 
			return -2;
		
		engines.clear();
		engines.resize(s);
		usedEngines.clear();
		usedEngines.resize(s, false);
//		fgetc(stdin);

		for (UINT sc = 0; sc < s; ++sc)
		{
			LPTSTR res = _fgetts(engines[sc].GetBuffer(100), 100, stdin);
			engines[sc].ReleaseBuffer();
			engines[sc].Trim();
			if (!res)
				return -3;
		};

		res = _ftscanf_s(stdin, _T("%u\n"), &q);
		if ((!res) || (res == EOF)) 
			return -4;

		queries.clear();
		queries.resize(q);

		for (UINT qc = 0; qc < q; ++qc)
		{
			LPTSTR res = _fgetts(queries[qc].GetBuffer(100), 100, stdin);
			queries[qc].ReleaseBuffer();
			queries[qc].Trim();
			if (!res)
				return -5;
		};

		freeEngines = s;
		switches = 0;
		
		for (UINT qc = 0; qc < q; ++qc)
		{
			//			UINT engine = std::find(usedEngines.begin(), usedEngines.end(), false);
			UINT engine = 0;
			std::vector<CString>::iterator itEngine = std::find(engines.begin(), engines.end(), queries[qc]);
			if (itEngine != engines.end())
				engine = UINT(itEngine - engines.begin());
			if (!usedEngines[engine])
			{
				if (freeEngines <= 1)
				{
					++switches;
					freeEngines = s;
					std::fill(usedEngines.begin(), usedEngines.end(), false);
				}

				--freeEngines;
				usedEngines[engine] = true;
			}
		};
		
		_ftprintf_s(stdout, _T("Case #%u: %u\n"), nc + 1, switches);
	};

	return 0;
}