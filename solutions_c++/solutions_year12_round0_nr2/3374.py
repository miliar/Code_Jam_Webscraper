//Dancing with Googlers 
//Google code jam 2012

#include<iostream>
#include<stdlib.h>

using namespace std;

int main()
{
  int count=0,T; // number of testcases
  cin>>T;
  //N S p <...>
  int N[T],S[T],p[T],*ni[T],ans[T],mainctr=0,surprisectr=0;
  while(count<T)
  {
    //Taking input the 'count' testcase
    cin>>N[count]>>S[count]>>p[count];
    ni[count] = new int[N[count]];
    for(int i=0;i<N[count];i++)cin>>ni[count][i];

    //Processing on the current testcase
    for(int i=0;i<N[count];i++)
      {
	//Unsurprising triplets minsum = 3*p-2 maxsum = 3*p
	if(ni[count][i]>=3*p[count]-2)mainctr++;
	//Surprising Ones
	else if(surprisectr<S[count])
	  {
	    if(p[count]>=2 && ni[count][i]>=3*p[count]-4)
	      {
		mainctr++;
		surprisectr++;
	      }
	    else if(p[count]==1 && ni[count][i]>=1)
	      {
		mainctr++;
		surprisectr++;
	      }
	    else {/*do nothing*/}
	  }
	else {/*do nothing */}
      }
    ans[count] = mainctr;
    count++;
    surprisectr=0;
    mainctr=0;
  }
  for(int i=0;i<T;i++)cout<<"Case #"<<i+1<<": "<<ans[i]<<endl;

  return 0;
}
