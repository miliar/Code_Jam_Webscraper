#include<iostream>
#include<cstdio>

using namespace std;

int main()
   {
      int t;
	  int surprise;
	  int count;
      int N, S, P;
	  int number;
      scanf("%d",&t);

	  int a=0;

      while(t--)
      {
          scanf("%d%d%d",&N,&S,&P);
          count=0;
		  surprise=0;

          while(N>0)
          {
              scanf("%d",&number);

              if((P*3)-number<=2)
                  count++;
              else if (((P*3)-number)<=4 && P>=2)
                  surprise++;

              N--;
          }

          if(surprise>S)
              surprise=S;

          count+=surprise;
          
          cout<<"Case #"<<a+1<<": "<<count<<endl;
          a++;
      }
      return 0;
   }
