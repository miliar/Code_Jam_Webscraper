#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <queue>
#define rep(X,Y) for ( int X=0; X<Y ; X++)
#define rep2(X,Y) for (  X=0; X<Y ; X++)
using namespace std;
void run(vector<int> &O,vector<int> &B,int o, int b,queue<char> &left,int T)
{
  int seconds=0;
  int iO=0,iB=0;
  int bPos=1,oPos=1;
  bool orange=false,blue=false;
  bool orangeValid=true,BlueValid=true;
  int len = max(o,b);
  while ( !left.empty())
    {
        if ( iO >= o )
        orangeValid=false;
        if(iB >= b)
        BlueValid=false;

      if (left.front() == 'B')
        {
          blue=true;
          orange = false;
          left.pop();

        }
      else
        {
          orange = true;
          blue = false;
          left.pop();
        }
      while (blue || orange)
        {


          if (O[iO] > oPos && B[iB]>bPos && orangeValid && BlueValid) //  move orange move blue
            {
              oPos++;
              bPos++;
         //     seconds++;
            }
          else if (O[iO] < oPos && B[iB]<bPos && orangeValid && BlueValid) //  move orange move blue
            {


                oPos--;


                bPos--;

      //          seconds++;
            }
          else if (O[iO] < oPos && B[iB]>bPos && orangeValid && BlueValid) //  move orange move blue
            {

                oPos--;

              bPos++;
      //        seconds++;
            }
          else if (O[iO] > oPos && B[iB]<bPos && orangeValid && BlueValid) //  move orange move blue
            {

              oPos++;
               bPos--;
      //        seconds++;
            }

        else  if (O[iO] >oPos && bPos == B[iB]&& blue && orangeValid && BlueValid) // move orange push blue
            {
              blue = false;

              oPos++;
              B[iB] = -1;
              //seconds++ ;
              iB++;
            }
          else if (O[iO] <oPos && bPos == B[iB]  && blue && BlueValid && orangeValid) // move orange push blue
            {
              oPos--;
              B[iB] = -1;
    //          seconds++ ;
              blue = false;
              iB++;
            }
            else if (O[iO]==oPos && B[iB]< bPos  && orange && orangeValid && BlueValid) //push orange Blue moves
            {
                  O[iO] = -1;
              orange = false;
     //         seconds++;
                bPos--;
              iO++;

            }
            else if (O[iO]==oPos && B[iB]> bPos  && orange && orangeValid && BlueValid) //push orange Blue moves
            {
                  O[iO] = -1;
              orange = false;
     //         seconds++;
                bPos++;
              iO++;

            }



          else if ( B[iB]>bPos && BlueValid)// move blue orange stays
            {
              bPos++;
      //        seconds++;
            }
          else if ( B[iB]<bPos && BlueValid )// move blue orange stays
            {
              bPos--;
     //         seconds++;
            }
          else if ( O[iO]>oPos &&orangeValid )// move orange blue stays
            {
              oPos++;
       //       seconds++;
            }
          else if ( O[iO]<oPos &&orangeValid )// move orange blue stays
            {
              oPos--;
  //            seconds++;
            }
          else if(B[iB] == bPos  &&blue && BlueValid) // pushblue orange stays
            {
              blue = false;
              B[iB] =-1;
   //           seconds++;
              iB++;

            }
            else if (O[iO]==oPos  && orange && orangeValid) //push orange Blue stays
            {
              O[iO] = -1;
              orange = false;
     //         seconds++;
              iO++;
            }
            seconds++;
        }

    }


    cout<<"Case #"<<T+1<<": "<<seconds<<endl;



}





int main()
{
  int T,N;
  freopen("A-large.in","r",stdin);
   freopen("output.txt","w",stdout);
  scanf("%d",&T);
  queue<char> Q;
  int o=0,b=0;
  char c;

  rep(X,T)
  {
    N=0;
    scanf("%d",&N);
    vector<int> O(N);
    vector<int> B(N);

    rep(i,N)
    {
      cin>>c;
  //    cout<<c;
      Q.push(c);
      if ( c=='O')
        cin>>O[o++];
      else
        cin>>B[b++];



    }

    run(O,B,o,b,Q,X);
    o=b=0;
  }

  return 0;
}
