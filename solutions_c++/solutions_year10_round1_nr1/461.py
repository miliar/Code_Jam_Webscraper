#include <iostream>
#include <vector>
#include <string>
#include <stdio.h>

using namespace std;

char bd[50][52];

int main(){
	string s;
	int len,N,K;
	char tmp[256];

	cin.getline(tmp,256);
	sscanf(tmp,"%d",&len);
	for(int i=0;i<len;++i)
	{
	  cin.getline(tmp,256);
	  sscanf(tmp,"%d %d",&N,&K);

	  for(int j=0;j<N;++j)
	  {
	    cin.getline(bd[j],N+2);
	  }


	  for(int j=0;j<N;++j){
	    int t = N-1;
	    for(int k=N-1;k>=0;--k)
	    {
	      if(bd[j][k]!='.')
	      {
		if(t!=k){
		bd[j][t] = bd[j][k];
		bd[j][k] = '.';}
		t--;
	      }
	    }
	  }

	  int red = 0;
	  int blue = 0;
	  for(int j=N-1;j>=0;--j){
	    if(bd[j][N-1]=='.')break;

	    for(int k=N-1;k>=0;--k){
	      char c = bd[j][k];
	      if(c=='.')break;
	      if(c=='R'&&red)continue;
	      if(c=='B'&&blue)continue;

	      int lc = 1,lr = 1,ln = 1,ln2 = 1;
	      for(int l=1;l<K;++l)
	      {
		if(lc && k-l >= 0 && bd[j][k-l]==c){++lc;}
		else lc = 0;

		if(lr && j-l >=0 && bd[j-l][k]==c){++lr;}
		else lr = 0;

		if(ln && j-l>=0 && k-l>=0 && bd[j-l][k-l]==c){++ln;}
		else ln = 0;

		if(ln2 && j-l<N && k+l<N && bd[j-l][k+l]==c){++ln2;}
		else ln2 = 0;
	      }

	      if(lc==K || ln==K || lr == K || ln2 == K)
	      {
		if(c=='R')red = 1;
		if(c=='B')blue = 1;
	      }
	    }
	  }

	  cout<<"Case #"<<(i+1)<<": ";
	  if(!red&&!blue)cout<<"Neither"<<endl;
	  else if(red&&!blue)cout<<"Red"<<endl;
	  else if(!red&&blue)cout<<"Blue"<<endl;
	  else cout<<"Both"<<endl;
	  /*
	  cout<<N<<" "<<K<<",R="<<red<<"B="<<blue<<endl;
	  for(int j=0;j<N;++j)
	    {
	    for(int k=0;k<N;++k){
	      cout<<bd[j][k];
	    }
	    cout<<endl;
	    }*/
	}

	return 0;
}
