#include<iostream>
#include<vector>
#include<string>
using namespace std;
char arr[100]="";
int main()
{ int T;
  cin>>T;
  for(int t=0;t<T;t++)
  { int L;
    cin>>L;
    string str="";
    for(int i=0;i<L;i++)
    { cin>>arr;
      int temp;
      cin>>temp;
      for(int j=0;j<temp;j++)
      str+=arr;
    }
    int curx=0,cury=0;
    int curdx=1,curdy=0;
    vector<int>x,y;
    x.push_back(curx);
    y.push_back(cury);
    int len=str.size();
    int mxx=0,mxy=0;
    int mnx=0,mny=0;
    for(int i=0;i<len;)
    { int newx=curx,newy=cury;
      char ch=str[i];
      int d=0;;
      while(i<len&&ch==str[i])
      { d++;  
        i++;
      }
      if(ch=='L')
      { if(curdx==1&&curdy==0)
        curdx=0,curdy=1;
        else if(curdx==0&&curdy==1)
        curdx=-1,curdy=0;
        else if(curdx==-1&&curdy==0)
        curdx=0,curdy=-1;
        else
        curdx=1,curdy=0;
      }
      else if(ch=='R')
      { if(curdx==1&&curdy==0)
        curdx=0,curdy=-1;
        else if(curdx==0&&curdy==-1)
        curdx=-1,curdy=0;
        else if(curdx==-1&&curdy==0)
        curdx=0,curdy=1;
        else
        curdx=1,curdy=0;
      }
      else
      { newx+=d*curdx;
        newy+=d*curdy;
        x.push_back(newx);
        y.push_back(newy);
        curx=newx;
        cury=newy;
        mxx=max(mxx,newx);
        mxy=max(mxy,newy);
        mnx=min(mnx,newx);
        mny=min(mny,newy);   
      }
    }
    //cerr<<mnx<<" "<<mxx<<" "<<mny<<" "<<mxy<<" ";
    long long area=0;
    int size=x.size();
    for(int i=mnx;i<mxx;i++)
    for(int j=mny;j<mxy;j++)
    { int left=0,right=0,top=0,bottom=0,valid=0;
      for(int k=0;k<size-1;k++)
      if(x[k]==x[k+1])
      { if(x[k]<=i&&min(y[k],y[k+1])<=j&&max(y[k],y[k+1])>=j+1)
        left=1;
        if(x[k]>=i+1&&min(y[k],y[k+1])<=j&&max(y[k],y[k+1])>=j+1)
        right=1;
      }
      else if(y[k]==y[k+1])
      { if(y[k]<=j&&min(x[k],x[k+1])<=i&&max(x[k],x[k+1])>=i+1)
        bottom=1;
        if(y[k]>=j+1&&min(x[k],x[k+1])<=i&&max(x[k],x[k+1])>=i+1)
        top=1;
      }
      if(left==right&&left==1||top==1&&top==bottom)
      valid=1;
      area+=valid;
    }  
    long long tarea=0;
    for(int i=1;i<size-1;i++)
    tarea+=x[i+1]*y[i]-x[i]*y[i+1];
    //cerr<<area<<" "<<abs(tarea)/2<<"\n";
    long long larea=area-abs(tarea)/2;
    cout<<"Case #"<<t+1<<": "<<larea<<"\n";
  }
}
    
    
