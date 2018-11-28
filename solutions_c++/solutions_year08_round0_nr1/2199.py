#include "iostream"
#include "fstream"
#include "string"
#include "vector"
#include "stdio.h"
using namespace std;

int main()
{
	int N,S,Q,i,engcount,pos,res,querycount;
	int ix,iy,max_pass,cur_pass,cur_pos;
	int count=1;
	ifstream ifile("d:\\in");
	ofstream ofile("d:\\out");
	char ch;
	string eng;
	vector<string> engstr;
	vector<int> query;
	ifile>>N;
	getline(ifile,eng);
	while (N)
	{
		i=0,engcount=0,pos=0,res=0;querycount=0,ix=0,iy=0;
		max_pass=0,cur_pass=0,cur_pos=0;
		eng="";
		engstr.clear();
		query.clear();
		ifile>>S;
		getline(ifile,eng);
	
		//scanf("%c",&ch);
		while (S)
		{
			/*scanf("%c",&ch);
			eng="";
			while(ch!='\n')
			{
				eng+=ch;
				scanf("%c",&ch);
			}*/

			
			getline(ifile,eng);
			engstr.push_back(eng);
			S--;
		}
		engcount=engstr.size();
		ifile>>Q;
		getline(ifile,eng);
		//scanf("%c",&ch);
		while (Q)
		{
			/*scanf("%c",&ch);
			eng="";
			while (ch!='\n')
			{
				eng+=ch;
				scanf("%c",&ch);
			}*/
			getline(ifile,eng);
			for(i=0;i<engcount;i++)
			{
				if(engstr[i]==eng)
					break;
			}
			query.push_back(i);
			Q--;
		}
		querycount=query.size();
		while(pos!=querycount)
		{
			max_pass=0;
			for (ix=0;ix<engcount;ix++)
			{
				cur_pass=0;
				for (iy=pos;iy<querycount;iy++)
				{
					if(query[iy]==ix)	
						break;
					cur_pass++;
				}	
				if(cur_pass>=max_pass)
				{
					max_pass=cur_pass;
					cur_pos=iy;
				}
			}
			if(cur_pos!=querycount)
				res++;
			pos=cur_pos;
		}
		ofile<<"Case #"<<count<<": "<<res<<endl;
		N--;
		count++;
	}


	return 1;
}