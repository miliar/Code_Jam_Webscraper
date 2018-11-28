#include <stdio.h>
#include <string>
#include <vector>
#include "stdlib.h"

using namespace std;
int LL,K,N;

string s;
vector<string> strs;

bool in(string s, char c)
{
  for (int i=0; i<s.size(); i++)
  {
    if (s[i] == c)
      return true;
  }
  return false;
}

int main()
{
   FILE* f = fopen("in.in", "r");
   FILE* out = fopen("out.out", "w");

   fscanf(f, "%d %d %d", &LL, &K, &N);

   fgetc(f);
   //char* s1 = (char*)malloc(sizeof(char) * (L+1));
  for (int i=0; i<K; i++)
  {
    for (int j=0; j<LL; j++)
    {
      char c;
      c = fgetc(f);
      s+=c;
    }
    fgetc(f);
    strs.push_back(s);
    s = "";
    /*s = "";
    for (int j=0; j<L; j++)
      s += s1[j];
    strs.push_back(s);*/
  }
  //fgetc(f);
  for (int i=0; i<N; i++)
  {
    s="";
    while(true)
    {
      char c;
      c = fgetc(f);
      if (c == '\n' || c == EOF)
      {
	break;
      }
      s+=c;
      
    }
    
    //fscanf(f, "%s", &s1);
    //s = s1;
    string temp = "";

    vector<string> sts;
    int globalcount = 0;
    bool flag = false;
    for (int j=0; j<s.size(); j++)
    {      
      if (s[j] == '(')
      {
	flag = true;
	  temp = "";
      }
      else
      {
	if (s[j] == ')')
	{
	  sts.push_back(temp);
	  flag = false;
	}
	else
	  if (flag)
	    temp+=s[j];
	  else
	    {
	      temp = "";
	      temp += s[j];
	      sts.push_back(temp);
	    }
      }
    }
    /*fprintf(out, "%d\n", sts.size());
    for (int j=0; j<sts.size(); j++)
    {
      for (int d=0; d<sts[j].size(); d++)
	fprintf(out, "%c", sts[j][d]);
      fprintf(out,"\n");
    }*/
    for (int j=0; j<strs.size(); j++)
    {
      int count = 0;
      

      
      for (int k=0; k<LL; k++)
      {
	//for (int l=0; l<sts.size(); l++)
	//{
	  //for (int d=0; d<sts[k].size(); d++)
	   // fprintf(out, "%c", sts[k][d]);
	  //fprintf(out, "\n");
	  //fprintf(out, "%c\n", strs[j][k]);
	//}
	if (in(sts[k],strs[j][k]))
	{
	  count++;
	}
	//fprintf(out, "%d\n", count);
      }
      if (count == LL)
      {
	globalcount++;
      }
    }
    fprintf(out, "Case #%d: %d\n", i+1, globalcount);

  }

fclose(out);
   fclose(f);
   return 0;
}