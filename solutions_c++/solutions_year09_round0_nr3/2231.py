#include<vector>
#include<map>
#include<set>
#include<string>
#include<algorithm>
#include<cmath>
#include<fstream>
#include<iostream>
using namespace std;
int main()
{
	ifstream  in("C-large.in.txt",ios::in);
    ofstream  out("output.txt");
	int msg[19][501];
	int N,i=0,j=0,k,p;
	in>>N;
    vector<string> words;
	string tp;
	getline(in,tp);
	while(i++<N)
	{
		getline(in,tp);
		words.push_back(tp);
	}
	tp="welcome to code jam";
	for(i=0;i<N;i++)
	{
        map<char,vector<int> > letters;
		for(j=0;j<tp.size();j++)
			if(letters.find(tp[j])==letters.end())
			{
				for(k=0;k<words[i].size();k++)
					if(words[i][k]==tp[j])  letters[tp[j]].push_back(k);
			}
		memset(msg,-1,sizeof(msg));
		for(j=0;j<tp.size();j++)
		{
			if(j>0)
			{
                for(k=0;k<letters[tp[j]].size();k++)
                    for(p=0;p<501&&p<letters[tp[j]][k];p++)
						if(msg[j-1][p]!=-1)
						{
                           if(msg[j][letters[tp[j]][k]]==-1) msg[j][letters[tp[j]][k]]=msg[j-1][p];
						   else 
						   {
							   msg[j][letters[tp[j]][k]]+=msg[j-1][p];
							   if(msg[j][letters[tp[j]][k]]>9999) msg[j][letters[tp[j]][k]]-=10000;
						   }
						}
			}
			else
			{
				for(k=0;k<letters[tp[j]].size();k++)
					msg[j][letters[tp[j]][k]]=1;
			}
		}
		string res="0000";
        int r=0;
        for(j=0;j<501;j++)
			if(msg[18][j]!=-1)  {r+=msg[18][j];if(r>9999) r-=10000;}
		for(j=3;j>=0;j--)
		{res[j]=r%10+'0';r/=10;}
		out<<"Case #"<<i+1<<": "<<res<<endl;
	}
}