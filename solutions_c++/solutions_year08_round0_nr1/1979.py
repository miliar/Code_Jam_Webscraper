#include <conio.h>
#include <stdio.h>
#include <vector>
#include <string>
#include <iostream>
 
#define MAXN 1005

bool path[MAXN][MAXN];

using namespace std;

int main() {
  int i,j,k;
  int n;
  FILE *fin,*fout;

  fin = fopen("a.in","r");
  fout = fopen("a.out","w");
  fscanf(fin,"%d",&n);
  
  for(int cases = 1;cases <= n;cases++) {
    int ns,nq;
    vector<string> s,q;
    vector<int> curr;
    vector<int> next;
    bool visited[MAXN];
    char temp[105];
    
    memset(path,0,MAXN*MAXN);
    memset(visited,0,MAXN);
    
    fscanf(fin,"%d",&ns);
    fgets(temp,101,fin);
    s.resize(ns);

    for(i = 0;i < ns;i++) {
      fgets(temp,101,fin);
      
      for(j = 0;temp[j] != '\0' && temp[j] != '\n';j++)
	s[i]+=temp[j];
    }

    
    /*fprintf(fout,"case %d %d\n",cases,ns);

    for(i = 0;i < ns;i++)
      fprintf(fout,"%s\n",s[i].c_str());
    */
      
    fscanf(fin,"%d",&nq);
    fgets(temp,101,fin);
    q.resize(nq);

    for(i = 0;i < nq;i++) {
      fgets(temp,101,fin);
      
      for(j = 0;temp[j] != '\0' && temp[j] != '\n';j++)
	q[i]+=temp[j];
    }
    
    
    /*fprintf(fout,"case %d %d\n",cases,nq);
	
    for(i = 0;i < nq;i++)
      fprintf(fout,"%s\n",q[i].c_str());
    */

    for(i = 0;i < ns;i++) {
      vector<int> occ;
      occ.push_back(-1);
      for(j = 0;j < q.size();j++)
	if(q[j] == s[i])
	  occ.push_back(j+1);
      occ.push_back(q.size()+1);
      
      /*fprintf(fout,"For %s\n",s[i].c_str());
      for(j = 0;j < occ.size();j++)
	fprintf(fout," %d",occ[j]);
	fprintf(fout,"\n");*/
      
      for(j = 0;j < occ.size()-1;j++) {
	for(k = occ[j]+1;k < occ[j+1];k++) {
	  path[k][occ[j+1]] = 1;
	  //fprintf(fout,"(%d,%d)",k,occ[j+1]);
	}
	//fprintf(fout,"\n");
      }
    }
    
    int nshift = 0;
    visited[0] = 1;
    curr.push_back(0);
    next.resize(0);
    
    while(!visited[nq+1]) {
      /*for(i = 0;i <= nq+1;i++)
	fprintf(fout,"%d ",visited[i]);
	fprintf(fout,"\n");*/
      nshift++;
      for(i = 0;i < curr.size();i++)
	for(j = curr[i]+1;j <= nq+1;j++)
	  if(path[curr[i]][j])
	    if(!visited[j]) {
	      next.push_back(j);
	      visited[j] = 1;
	    }
      curr.resize(next.size());
      curr = next;
      next.resize(0);
    }
    
    fprintf(fout,"Case #%d: %d\n",cases,nshift-1);
    }
  
  fclose(fin);
  fclose(fout);
  
  return 0;
  }
