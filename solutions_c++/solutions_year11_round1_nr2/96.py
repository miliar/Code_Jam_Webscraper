#include <stdio.h>
#include <math.h>
#include <map>
#include <vector>
#include <string>
#include <iostream>
using namespace std;
string words[20000];
map<pair<string,int>,bool> counts;
int Points[20000];
int N,M;
int main()
{
  int T;
  cin>>T;
  for(int t=1;t<=T;t++)
    {
      cout << "Case #" << t << ": ";
      cin>>N>>M;
      for(int i=0;i<N;i++)
	{
	  //printf("%d\n",i);
	  string word;
	  cin>>word;
	  words[i]=word;
	}
      // printf("sdfs\n");
      for(int i=0;i<M;i++)
	{
	  string seq;
	  cin>>seq;
	  counts.clear();
	  //printf("%d\n",i);
	  for(int j=0;j<N;j++)
	    {
	      //printf("%d\n",j);
	      string word=words[j];
	      string guess=word;
	      for(int k=0;k<guess.size();k++)
		guess[k]='_';
	      for(int p=0;p<seq.size();p++)
		{
		  string nextguess=guess;
		  bool there=false;
		  for(int k=0;k<word.size();k++)
		    {
		      if(word[k]==seq[p])
			{
			  nextguess[k]=word[k];
			  there=true;
			}
		    }
		  if(there)
		    counts[make_pair(guess,p)]=true;
		  guess=nextguess;
		}
	    }
	  //printf("sdfsd\n");
	  
	  int maxpts=0;
	    for(int j=0;j<N;j++)
	      {
		Points[j]=0;
		string word=words[j];
		string guess=word;
		for(int k=0;k<guess.size();k++)
		  guess[k]='_';
		for(int p=0;p<seq.size();p++)
		  {
		    bool there=false;
		    string nextguess=guess;
		    for(int k=0;k<word.size();k++)
		      {
			if(word[k]==seq[p])
			  {
			    nextguess[k]=word[k];
			    there=true;
			  }
		      }
		    if(!there && counts.find(make_pair(guess,p))!=counts.end())
		      Points[j]++;
		    guess=nextguess;
		  }
		maxpts=max(maxpts,Points[j]);
	      }
	    string target;
	    for(int j=0;j<N;j++)
	      {
		if(Points[j]==maxpts)
		  {
		    target=words[j];
		    break;
		  }
	      }
	    
	    cout << target <<  " " ;
	  
	  

	}
      cout << endl;
    }
}
