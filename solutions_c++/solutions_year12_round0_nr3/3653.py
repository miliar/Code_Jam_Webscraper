#include<iostream>
using namespace std;
int Arr1[100],Arr2[100],idx1,idx2;

int find(int x)
{
    for(int i=0;i<idx1;i++)
    {
            if(x==Arr2[i])return i;
    }
    return -1;
}

void shifttoArr(int A,int B)
{
     idx1=0;
     while(B!=0 || A!=0)
     {
                Arr1[idx1]=(A%10);
                Arr2[idx1]=(B%10);
                idx1++;
                A=A/10;
                B=B/10;
     }
}

void shift1()
{
     int temp,i;
     temp=Arr2[0];
    for(i=0;i<idx1-1;i++)
    {
            Arr2[i]=Arr2[i+1];
    }
    Arr2[i]=temp;
}

int isSame()
{
    for(int i=0;i<idx1;i++)
    {
                         if(Arr1[i]!=Arr2[i])return 0;
    }
    return 1;
}

int Pair(int A, int B)
{
    int idxB,sumA=0,sumB=0,tmp;
    tmp=A;
    shifttoArr(A,B);
    for(int i=0;i<idx1;i++)
    {
            if(isSame())return 1;
            else
            shift1();
    }
    /*
    idxB=find(Arr1[idx1-1]);
    if(idxB==-1)return 0;
    cout<<endl<<"start"<<endl;
    for(int i=idx1-1;i>=0;i--,idxB--)
    {
            
            if(idxB==-1)idxB=idx1-1;
            cout<<idxB<<" "<<i<<"="<<Arr2[idxB]<<"-"<<Arr1[i]<<endl;
            if(Arr2[idxB]!=Arr1[i]) return 0;
    }
    cout<<idx1<<" "<<A<<" "<<B<<endl;
    
   for(int i=idx1-1;i>=0;i--)
   cout<<Arr2[i];
    cout<<" "<<idxB<<" "<<tmp<<"-"<<B<<endl;
    */
    return 0;
}

int main()
{
    int N,A,B,res;
    cin>>N;
    for(int i=1;i<=N;i++)
    {
            res=0;
            cin>>A;
            cin>>B;
           
            for(int j=A;j<B;j++)
            for(int k=j+1;k<=B;k++)
            {
                    if(j==k)
                    {}
                    else if(Pair(j,k))
                    res++;
            }
       
      // Pair(112,211);     
            cout<<"Case #"<<i<<": "<<res<<endl;
    }
    return 0;
}
