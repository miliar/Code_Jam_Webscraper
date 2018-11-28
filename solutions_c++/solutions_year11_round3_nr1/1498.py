  #include "iostream.h"
  int T, R,C;
  
  int main(){
    int k=0, i;
	int impossible;
    cin >>T;
	char a;
    char M[50][50];

    while (T-->0){
      k++;
	  impossible = 0;
	  cin >> R;
	  cin >> C;
      for (i = 0; i<R; i++){
		for(int j=0;j<C; j++)
		{
			cin>>M[i][j];
			//cout<<M[i][j];
		}
		cout <<endl;
      }
      for (i = 0; i<R; i++){
		for(int j=0;j<C; j++)
		{
			if(M[i][j] == '#')
			{
				if (i==R-1 || j==C-1)
				{
					impossible = 1;
					break;
				}
				else if (M[i+1][j]=='#' && M[i+1][j+1]=='#' && M[i][j+1]=='#')
				{
					M[i][j] = '/';
					M[i+1][j]='\\';
					M[i+1][j+1]='/';
					M[i][j+1]='\\';
				}
				else
				{
					impossible = 1;
					break;
				}				
			}
			if (impossible) break;
		}   
		if (impossible) break;
	  }
	  cout << "Case #" << k << ":"<<endl;
	  if(impossible) cout << "Impossible" <<endl;
      else 
	  {
	    for (i = 0; i<R; i++){
			for(int j=0;j<C; j++)
			{
				cout<<M[i][j];
			}
			cout<<endl;
		}
	  }
	}
    return 1;
  }

