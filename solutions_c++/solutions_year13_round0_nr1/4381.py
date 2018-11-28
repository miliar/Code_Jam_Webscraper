#include <iostream>
#include <string>

using namespace std;

int check(int val)
{
	int local=0;
	switch (val)
	{
	    case 40:
	    case 1030: local=-1; break;
		case 400:
		case 1300: local=1; break;
     }
	return local;
}
        int main()     {
          int T;
		  string line;
          cin>>T;
		  for (int m = 0;m<T;m++)
		  {
	          getline(cin, line);
			  int R[4]={0,0,0,0};
			  int C[4]={0,0,0,0};
			  int D[2]={0,0};
			  bool hasEmpty=false;
			  int res=0;
			  for (int i=0;i<4;i++)
			  {
				  for (int j=0;j<4;j++)
				  {
					  char tmp;
					  int val=0;
					  cin>>tmp;
					  switch (tmp)
					  {
						  case 'X': val=100; break;
						  case 'O': val=10; break;
					      case 'T': val=1000; break;
						  case '.': val=0; hasEmpty=true; break;
					  }
					  R[i]+=val;
					  C[j]+=val;
					  if (i==j) D[0]+=val;
					  if (i+j==3) D[1]+=val;

				  }
			  }
			  for (int x=0; x<4;x++)
			  {
				  res+= check(R[x]);
				  res+= check(C[x]);
			  }

			  res+= check(D[0]);
			  res+= check(D[1]);


		  cout<<"Case #"<<m+1<<": ";
		  if (res<0) cout<<"O won";
		  else if (res>0) cout<<"X won";
		  else if ( (res==0) && hasEmpty) cout<<"Game has not completed";
		  else cout<<"Draw";
		  cout<<endl;
		  }

          return 0;
        }