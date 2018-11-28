#include <cstdio>
#include <list>
#include <utility>
#include <algorithm>
using namespace std;

int main(){
  int T;
  scanf("%d",&T);
  for(int nrt=1; nrt<=T; nrt++){
	int n;
	scanf("%d",&n);
	pair<int,int> rows[n];
	int positions[n];
	int tablica[n];
	bool reserved[n];
	for(int i=0; i<n; i++)
	  reserved[i]=false;
	char temp[n+1];
	for(int i=0; i<n; i++){
	  scanf("%s",temp);
	  rows[i].second=i;
	  int x=0;
	  for(int j=0; j<n; j++){
	     if(temp[j]=='1')x=j;
	  }
	  while(reserved[x])x++;
	  rows[i].first=x;
	  reserved[x]=true;
	}
	sort(rows,rows+n);
	for(int i=0; i<n; i++){
	   positions[i]=tablica[i]=i;
	}
	int res=0;
	for(int i=n-1; i>0; i--){
	  int k=rows[i].second;
	  int docpos=rows[i].first;
//	  int docpos=i;
	  while(positions[k]<docpos){
	    int temp1=tablica[positions[k]+1];
	    positions[k]++;
	    positions[temp1]--;
	    res++;
	    tablica[positions[k]]=k;
	    tablica[positions[temp1]]=temp1;	
	  }
	}
	printf("Case #%d: %d\n",nrt,res);
   }
}

