#include<iostream>
#include<fstream>
#include<vector>

using namespace std;

main(){
  int T,C,D,N,fin;
  char n[100];
  int c[26][26],d[26][26];
  int ind[26];
  int i,j,k,l;
  char c1,c2,c3;
  ifstream ifs("B-large");
  ofstream ofs("ans-b");

  ifs>>T;
  for(i=1;i<=T;++i){
    fin = 0;
    for(j=0;j<26;++j)
      for(k=0;k<26;++k)
	c[j][k]=d[j][k]=0;

    for(j=0;j<26;++j)
      ind[j] = 0;

    ifs>>C;

    for(j=0;j<C;++j){
      ifs>>c1>>c2>>c3;
      c[(int)c1-65][(int)c2-65] = c[(int)c2-65][(int)c1-65] = (int)c3;
    }

    ifs>>D;
    for(j=0;j<D;++j){
      ifs>>c1>>c2;
      d[(int)c1-65][(int)c2-65] =  d[(int)c2-65][(int)c1-65] = 1;
    }

    ifs>>N;
    for(j=0;j<N;++j){
      ifs>>n[fin];
      if(c[(int)n[fin]-65][(int)n[fin-1]-65] && fin){
	cout<<i<<"\t"<<n[fin-1]<<n[fin]<<endl;
	ind[(int)n[fin-1]-65]--;
	n[fin-1] = (char)(c[(int)n[fin]-65][(int)n[fin-1]-65]);
	--fin;
      }
      else{
	
	for(k=0;k<26;++k){
	  if(ind[k] && d[k][(int)n[fin]-65]){
	    for(l=0;l<26;++l)
	      ind[l] = 0;
	    cout<<i<<"\t"<<(char)(k+65)<<n[fin]<<endl;

	    fin = -1;
	    break;
	  }
	}
	if(k==26)
	  ind[(int)n[fin]-65]++;
      }
      ++fin;
    }

    if(fin){
      ofs<<"Case #"<<i<<": ["<<n[0];
      for(j =1;j<fin;++j)
	ofs<<", "<<n[j];
      ofs<<"]"<<endl;
    }
    else
      ofs<<"Case #"<<i<<": []"<<endl;;

  }
  ifs.close();
  ofs.close();
}
