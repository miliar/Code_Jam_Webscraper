#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
 
using namespace std;
 
 bool good(vector < int > h, int x) { 
		int prev = 0, n = h.size();
		

		for(int i=0;i<=n-1;i++) {
			//if we can make tree[i] higher than previous one
			if (h[i] + x <= prev) return false;
			//reset the value of prev for the next step
			prev = max(prev + 1, h[i] - x);
		}
		return true;
	}
 

  int minLevel(vector <int> heights) {
    int left=-1;
    int right=1000000000;
    while(right>left+1){
      int mid=(left+right)/2;
      if(good(heights,mid)) right=mid;
      else left=mid;
    }
    return right;
  }
int main()
{
    int xtest,xi,xj,xt,xk,xX,xO,xfreqdot,xresult,xdot;
    string xarr[4];
    int xct=0;
    
    vector<int>v;
    v.push_back(5);
    bool ll= good(v,0);
    
    
    char xc,xd;
    cin>>xtest;
    while(xtest--)
    {
        for(xi=0;xi<4;xi++)
        {
            cin>>xarr[xi];
            //cout<<arr[i]<<"\n";;
        }
        xresult=0;
        xdot=xX=xO=xt=0;
        minLevel(v);
        //horizontal
        for(xi=0;xi<4;xi++)
        {
            xX=xO=xt=0;
            for(xj=0;xj<4;xj++)
            {
                if(xarr[xi][xj]=='.')
                    xdot++;
                else if(xarr[xi][xj]=='T')
                    xt++;
                else if(xarr[xi][xj]=='X')
                    xX++;
                else if(xarr[xi][xj]=='O')
                    xO++;
            }
            if(xX==4 || (xX==3 && xt==1))
            {
                    xresult=1;
                    break;
            }
            if(xO==4 || (xO==3 && xt==1))
            {
                    xresult=2;
                    break;
            }
        }
        
        char a[4][4];
      int i,j;
        
        xX=xO=xt=0;
        if(xresult==0)
        {
            //vertical
            for(xj=0;xj<4;xj++)
            {
                xX=xO=xt=0;
                for(xi=0;xi<4;xi++)
                {
                    if(xarr[xi][xj]=='.')
                        xdot++;
                    else if(xarr[xi][xj]=='T')
                        xt++;
                    else if(xarr[xi][xj]=='X')
                        xX++;
                    else if(xarr[xi][xj]=='O')
                        xO++;
                }
                if(xX==4 || (xX==3 && xt==1))
                {
                        xresult=1;
                        break;
                }
                if(xO==4 || (xO==3 && xt==1))
                {
                        xresult=2;
                        break;
                }
            }
        }
        xX=xO=xt=0;
        bool ans;
        for(i=0;i<4;i++) for(j=0;j<4;j++)
      {
         if(i==3||j==3) continue;
         
         int sum=0;
         if(a[i][j]=='#') sum++;
         if(a[i+1][j]=='#') sum++;
         if(a[i][j+1]=='#') sum++;
         if(a[i+1][j+1]=='#') sum++;
         
         if(sum==0||sum==1||sum==3||sum==4) {ans=true; break;}
         }
         
         
        if(xresult==0)
        {
            
            for(xj=0;xj<4;xj++)
            {
                for(xi=xj;xi<xj+1;xi++)
                {
                    if(xarr[xi][xj]=='.')
                        xdot++;
                    else if(xarr[xi][xj]=='T')
                        xt++;
                    else if(xarr[xi][xj]=='X')
                        xX++;
                    else if(xarr[xi][xj]=='O')
                        xO++;
                }
                if(xX==4 || (xX==3 && xt==1))
                {
                        xresult=1;
                        break;
                }
                if(xO==4 || (xO==3 && xt==1))
                {
                        xresult=2;
                        break;
                }
            }
        }
         xX=xO=xt=0;
        if(xresult==0)
        {
           
            for(xj=0;xj<4;xj++)
            {
                for(xi=3-xj;xi<3-xj+1;xi++)
                {
                    if(xarr[xi][xj]=='.')
                        xdot++;
                    else if(xarr[xi][xj]=='T')
                        xt++;
                    else if(xarr[xi][xj]=='X')
                        xX++;
                    else if(xarr[xi][xj]=='O')
                        xO++;
                }
                if(xX==4 || (xX==3 && xt==1))
                {
                        xresult=1;
                        break;
                }
                if(xO==4 || (xO==3 && xt==1))
                {
                        xresult=2;
                        break;
                }
            }
        }
        xct++;
        if(xresult==1)
            cout<<"Case #"<<xct<<": X won";
        else if(xresult==2)
            cout<<"Case #"<<xct<<": O won";
        else if(xdot>0)
            cout<<"Case #"<<xct<<": Game has not completed";
        else cout<<"Case #"<<xct<<": Draw";
        cout<<"\n";
    }

}













