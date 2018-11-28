#include <iostream>
#include <math.h>
using namespace std;

void main()
{
	_int64 case_num;
	cin >> case_num;
	_int64 *snap_num = (_int64 *) malloc (sizeof(_int64) * case_num);
	_int64 *time_snap = (_int64 *) malloc (sizeof(_int64) * case_num);

	_int64 i;
	for (i = 0; i < case_num; ++i)
	{
		cin >> snap_num[i] >> time_snap[i];
		if ((time_snap[i] + 1) % int(pow(2, double(snap_num[i]))) == 0)
			printf("Case #%I64d: ON\n", i+1);
		else printf("Case #%I64d: OFF\n", i+1);
	}




	free (snap_num);
	free (time_snap);

}