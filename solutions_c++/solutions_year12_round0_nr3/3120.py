#include "Common.h"

void main()
{
	FileIO		file;
	Display		dis;
	Tokenizer	tok;
	strarr		arr;
	strarr		out;
	file.read(arr, "C-small-attempt1.in");
	//dis.show(arr);
	for(string::size_type i=1 ; i<arr.size() ; i++)
	{
		string &line = arr.at(i);
		strarr token;
		char buf[16];
		tok.tokenize(token, line);
		vector<int> token_i;
		int min = atoi(token[0].c_str());
		int max = atoi(token[1].c_str());
		int rec = 0;
		for(int m=min+1 ; m<=max ; m++)
		{
			string ms(itoa(m, buf, 10));
			for(int n=min ; n<m ; n++)
			{
				string ns(itoa(n, buf, 10));
				for(int ctr=0 ; ctr<ns.length() ; ctr++)
				{
					char end = ns[ns.size()-1];
					ns.erase(ns.end()-1);
					ns.insert(ns.begin(), end);
					if(end == '0')
					{	continue;}
					if(ns==ms)
					{
						rec++;
					//	cout<<n<<" "<<m<<" "<<ns<<" "<<ms<<"\n";
					}
				}
			}
		}
		string	res("Case #");
		res.append(_itoa(i,buf,10));
		res.append(": ");
		res.append(_itoa(rec,buf,10));
		out.push_back(res);
	}
	dis.show(out);
	//dis.show(outline);
	file.write(out);
	getch();
}