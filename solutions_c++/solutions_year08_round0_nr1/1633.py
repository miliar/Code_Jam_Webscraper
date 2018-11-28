#include <cstdio>
#include <iostream>

using namespace std;

int main(){

  int zest,i,n,z,j,m;
  string szukacze[200];
  string dane[2000];
  string tmp;

  int tab[110][1100];

  cin >> zest;

  for(z=1;z<=zest;z++){
    /////////////////////////////////////
    cin >> n;
    getline(cin,tmp);
    //cout << "n="<<n<<endl;
    for(i=0;i<n;i++){
      getline(cin,szukacze[i]);
      //cout <<"szukacz:"<< szukacze[i]<<endl;
    }
    cin >> m;
    getline(cin,tmp);
    //cout << "m="<<m<<endl;
    for(i=0;i<m;i++){
      getline(cin,dane[i]);
      //cout << dane[i]<<endl;
    }

    for(i=0;i<n;i++){
      tab[i][m]=0;
    }
    for(i=0;i<n;i++){
      for(j=m-1;j>=0;j--){
	if(szukacze[i]!=dane[j]){
	  tab[i][j]=tab[i][j+1]+1;
	}else{
	  tab[i][j]=0;
	}
      }
    }
    /*
    for(j=0;j<=m;j++){
      for(i=0;i<n;i++){
	cout << tab[i][j] <<" ";
      }
      cout <<endl;
    }
    //*/
    int koniec=0;
    int max,maxi,wynik=-1;
    while(koniec<m){
      max=-1;maxi=-1;
      for(i=0;i<n;i++){
	if(tab[i][koniec]>max){
	  max=tab[i][koniec];
	  maxi=i;
	}
      }
      //cout <<"ide " << max <<" pol  na " <<maxi<<endl;
      koniec+=max;
      wynik++;
    }
    if(m==0){
      wynik=0;
    }
    cout<<"Case #"<<z<<": "<<wynik<<endl;






    //////////////////////////////
  }
  return 0;
}





