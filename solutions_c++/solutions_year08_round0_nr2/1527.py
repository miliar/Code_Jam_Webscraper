#include<iostream>
#include<string>
using namespace std;

struct tim
{int h;
 int m;};

int sortt(tim  arr[100],int n)
{ int i=0,j=0,k=0;
   tim temp;
  for(i=0;i<n;i++)
   { k=i;
     for(j=i+1;j<n;j++)
      if(arr[j].h<arr[k].h || ( arr[j].h==arr[k].h && arr[j].m<arr[k].m))
         k=j;
      if(k!=i)
       {temp=arr[i];
        arr[i] = arr[k];
        arr[k]=temp;
        }
      
         
    }
  return 0;
 }

int main()
{
 int N=0,i=0,j=0,k=0,na=0,nb=0,NA=0,NB=0,ta=0,tb=0,T=0,l=0;
 string in;
 tim TAd[100],TAa[100];
 tim TBd[100],TBa[100];
//cout<<"a";
 cin>>N;
for(l=0;l<N;l++)
 {
  
 cin>>T;
 cin>>NA>>NB;


 for( i=0;i<NA;i++)
 { cin>>in;
   TAd[i].h=(in[0]-48)*10+(in[1]-48);
   TAd[i].m=(in[3]-48)*10+(in[4]-48);
    //cout<<TAd[i].h<<" "<<TAd[i].m<<endl;
   cin>>in;
   TBa[i].h=(in[0]-48)*10+(in[1]-48);
   TBa[i].m=(in[3]-48)*10+(in[4]-48);
    //cout <<TBa[i]<<endl;
   }
 // for(i=0;i<NA;i++)
  // cout<<TAd[i].m<<" ";
  //cout<<endl;
 sortt(TAd,NA);
//  for(i=0;i<NA;i++)
 //  cout<<TAd[i].m<<" ";
 sortt(TBa,NA);

 for( i=0;i<NB;i++)
 { cin>>in;
   TBd[i].h=(in[0]-48)*10+(in[1]-48);
   TBd[i].m=(in[3]-48)*10+(in[4]-48);
    //cout<<in[0]*10<<" "<<(int)in[1]<<endl;
   cin>>in;
   TAa[i].h=(in[0]-48)*10+(in[1]-48);
   TAa[i].m=(in[3]-48)*10+(in[4]-48);
    //cout <<TBa[i]<<endl;
   }
 sortt(TAa,NB);
 sortt(TBd,NB);
for(i=0,j=0,ta=0,na=0;i<NB&&j<NA;)
  { if(TAa[i].h*60+TAa[i].m+T<=TAd[j].h*60+TAd[j].m)//if(TAa[i].h<TAd[j].h || ( TAa[i].h==TAd[k].h && TAa[i].m+T<=TAd[j].m))
      {ta++;
       i++;
       }
       else
       { if(ta!=0)
         { ta--;
          j++;
         }
         else
          { na++;
           // cout<<TAd[j].m<<" "<<i<<" "<<j<<endl;
            j++;
           }
        }
   }
 if(j<NA)
  { k=j+ta-NA;
   if(k<0)
     na-=k;
   }
for(i=0,j=0,tb=0,nb=0;i<NA&&j<NB;)
  { if(TBa[i].h*60+TBa[i].m+T<=TBd[j].h*60+TBd[j].m)//if(TBa[i].h<TBd[j].h || ( TBa[i].h==TBd[k].h && TBa[i].m+T<=TBd[j].m))
      {tb++;
       i++;
       }
       else
       { if(tb!=0)
         { tb--;
          j++;
         }
         else
          { nb++;
            j++;
           }
        }
   }
 if(j<NB)
  { k=j+tb-NB;
   if(k<0)
     nb-=k;
   }

cout<<"Case #"<<l+1<<": "<<na<<" "<<nb<<endl;
}
return 0;
}
