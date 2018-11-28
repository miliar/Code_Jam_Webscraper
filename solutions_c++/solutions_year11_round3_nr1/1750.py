#include<iostream>
#include<math.h>
#include<String.h>
#include<fstream.h>
using namespace std;
#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)

long double wp(int arr[100][100], int team, int n)
{
  long double cpll=0, cneg=0;
  for(int i=0;i<n;i++)
  {
    if(arr[team][i]==1)
    {
      cpll++;
      cneg++;
    } else if(arr[team][i]==0)
    cneg++;  
  }
  if(cneg!=0)
  return cpll/cneg;
  else
  return 0;
}

long double owp(int arr[100][100], int team, int n)
{
  int i,j;
  int arr1[100][100];
  for(i=0;i<100;i++)
    for(j=0;j<100;j++)
      arr1[i][j] = arr[i][j];
  long double sum=0, WP=0;
  int games=0;
  
  for(i=0;i<n;i++)
  {
    if(arr1[i][team] == 1 || arr1[i][team] == 0)
    {
      arr1[i][team] = -10;
      games++;
       
      //cout<<"here";
      }
  }
  for(i=0;i<n;i++)
  {
  
    if(arr1[i][team] == -10)
    {
     WP=wp(arr1,i,n);
     //cout<<"WP  " << WP<<endl;
     sum+=WP;
     }
     
  }
  //cout<<"sum: "<<sum<<"games: "<< games<<endl<<endl;
  //return sum/(n-1);
  if(games!=0)
  return sum/games;
  else 
  return 0;
}

long double oowp(int arr[100][100], int team, int n)
{
   int op = 0,i;
   long double sum = 0.0;
   long double val=0.0;
   
   for(i=0;i<n;i++)
   {
     if(arr[team][i]==0|| arr[team][i]==1)
     {  op++;
      sum+=owp(arr,i,n);
     }
     
   }
   //cout<<"sum: "<<sum<<" op: "<<op<<endl;
   if(op!=0)
     return sum/op;
   else
     return 0;
}

int main()
{
	int T,N,B_pos = 1, O_pos = 1,*cpos,pos=0,can =0,i,sec=1,change;

	char *color;
    int d,l;
	ofstream out;
	ifstream in;
	in.open("in.txt");
	out.open("out.txt");
	in>>T;
	cout<<"#testcases"<<T<<endl;
	int counter = 1;
	int j,r,c;
	int n;
	long double WP =0.0, OWP=0.0, OOWP=0.0, RPI=0.0;
	char arr[50][50];
	char arr1[50][50];
	int imp = 0;
	for(counter=1; counter<=T; counter++)
	{
      imp =0;
      out<<"Case #"<<counter<<":"<<endl;
      in>>r;
      in>>c;
      REP(i,r)
      {
        REP(j,c)
        {
          in>>arr[i][j];
          arr1[i][j] = arr[i][j];
          cout<<arr[i][j];
        } 
         cout<<endl;
      }
      
      REP(i,r)
      {
        REP(j,c)
        {
          if(arr[i][j] == '#')
          {
            cout<<"";
            if(arr[i+1][j] == '#' && arr[i][j+1] == '#' && arr[i+1][j+1] == '#')
            {
              arr[i][j] = arr[i+1][j+1] = '/';
              arr[i+1][j] = arr[i][j+1] = '\\';
            } else
              {
                  cout<<"impossi"<<i<<" "<<j;
                  imp = 1;
              }
           }
        }
      
      }
      cout<<"case "<<counter<<" impval: "<<imp<<endl;
      //out<<"Case #"<<counter<<":"<<endl;
      if(imp==1)
      {
      out<<"Impossible"<<endl;
        
      } else
      {
      REP(i,r)
      {
        REP(j,c)
        {
          cout<<arr[i][j];
          out<<arr[i][j];
        }
          cout<<endl;
          out<<endl;
      }
      }
      cout<<"\n\n\n";
                      
	}
	getchar();
}

