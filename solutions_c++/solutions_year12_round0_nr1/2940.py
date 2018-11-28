#include "Common.h"

void main()
{
	FileIO		file;
	Display		dis;
	strarr		arr;
	strarr		outline;
	file.read(arr, "A-small-attempt0.in");
	//dis.show(arr);
	for(string::size_type i=1 ; i<arr.size() ; i++)
	{
		string& word = arr.at(i);
		string	trans("Case #");
		char buf[8];
		trans.append(_itoa(i,buf,10));
		trans.append(": ");
		for(int k=0 ; k<word.size() ; k++)
		{
			char inp[] = "ejp mysljylc kd kxveddknmc re jsicpdrysi\
						rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd\
						de kr kd eoya kw aej tysr re ujdr lkgc jvqz";
			char out[] = "our language is impossible to understand\
						there are twenty six factorial possibilities\
						so it is okay if you want to just give upzq";
			char ltr = word.at(k);
			int lt;
			for(lt=0 ; inp[lt]!='\0' ; lt++)
			{
				if(inp[lt] == ltr)
				{
					trans.push_back(out[lt]);
					break;
				}
				if(inp[lt] == '\n')
					break;
			}
		}
		outline.push_back(trans);
	}
	//dis.show(outline);
	file.write(outline);
	getch();
}