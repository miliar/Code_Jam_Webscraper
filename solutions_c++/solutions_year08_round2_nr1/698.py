#include<iostream>
//#include<conio.h>
#include<vector>

using namespace std;

typedef long long LL;

int main(int argc, char *argv[])
{
  int cases, N;
  LL n, A, B, C, D, x0, y0, M, triangs;

  LL X, Y, i, j, k, x1, y1, x2, y2, x3, y3;

  cin>>cases;
  for(N=1;N<=cases;N++)
  {
   vector<LL> x, y;//, idx;
   cin>>n>>A>>B>>C>>D>>x0>>y0>>M;

   X = x0; Y = y0;
   x.push_back(X); y.push_back(Y); //idx.push_back(0);
   //cout<<X<<", "<<Y<<endl; //print X, Y
   for(i=1;i<n;i++)
   {
       X = (A * X + B) % M;
       Y = (C * Y + D) % M;
       x.push_back(X); y.push_back(Y); //idx.push_back(i);
       //cout<<X<<", "<<Y<<endl; //print X, Y
   }

   triangs=0;
   //do
   //{

   //} while(next_permutation(idx.begin(), idx.end()));
   for(i=0;i<n;i++)
   {
    x1=x[i]; y1=y[i];
    for(j=i+1;j<n;j++)
    {
     if(i==j) continue;
     x2=x[j]; y2=y[j];
     for(k=j+1;k<n;k++)
     {
      if(j==k||i==k) continue;
      x3=x[k]; y3=y[k];

      X=(x1+x2+x3);
      Y=(y1+y2+y3);
      if(X%3==0&&Y%3==0)
       triangs++;
     }
    }
   }
   cout<<"Case #"<<N<<": "<<triangs<<endl;
  }
  //cin>>N; //just to pause
  return 0;
}
