#include<iostream>
#include<cstring>
#include<set>

#define HEIGHT 100
#define WIDTH  100
#include<stack>
using namespace std;
struct cell
{
    cell():altitudes(0),basin(0){direction=0;}
    int altitudes;
    char basin;
   // char is_sink;//0for init   1 for not   2 for yes
    char direction;//0 for init 1 for sink 2 for North 3 for west  4 for east 5 for south
	void clear(){altitudes=0;basin=0;direction=0;}
};

cell cell_array[HEIGHT][WIDTH];
int Goodindex(int max_h,int max_w,int i, int j,int direction)
{
    if (direction == 0)//north
    {
       if(i-1>=0)
        return 1;
       else
        return 0;
    }
     if (direction == 1)//west
    {
       if(j-1>=0)
        return 1;
       else
        return 0;
    }
    if (direction == 2)//east
    {
       if(j+1<max_w)
        return 1;
       else
        return 0;
    }
     if (direction == 3)//north
    {
       if(i+1<max_h)
        return 1;
       else
        return 0;
    }
    return 0;

}


struct numpair
{
	numpair():i(0),j(0){}
	int i,j;
};
int main()
{
    int T,numT;
    int H,W;
    cin>>T;
    numT=T;
    int type;
    int temphigh=0;
    char nowget;
	stack<numpair> ijpair;
	numpair mymn;
    while(numT--)
    {
       nowget='a';
      cin>>H>>W;
      for(int i=0 ; i<H; i++)
        for(int j=0; j<W; j++)
        {
			cell_array[i][j].clear();
            cin >> cell_array[i][j].altitudes;
            if(i==0&&j==0)
                cell_array[i][j].basin=nowget++;
        }
      for(int i=0 ; i<H; i++)
        for(int j=0; j<W; j++)
        {
            if(cell_array[i][j].direction==0)
            {

                temphigh=cell_array[i][j].altitudes;
                if(Goodindex(H,W,i,j,0))
                {
                    if(temphigh > cell_array[i-1][j].altitudes)
                    {
                        temphigh=cell_array[i-1][j].altitudes;
                        cell_array[i][j].direction=2;
                    }
                }
                if(Goodindex(H,W,i,j,1))
                {
                    if(temphigh > cell_array[i][j-1].altitudes)
                    {
                        temphigh=cell_array[i][j-1].altitudes;
                        cell_array[i][j].direction=3;
                    }
                }
                if(Goodindex(H,W,i,j,2))
                {
                    if(temphigh > cell_array[i][j+1].altitudes)
                    {
                        temphigh=cell_array[i][j+1].altitudes;
                        cell_array[i][j].direction=4;
                    }
                }
               if(Goodindex(H,W,i,j,3))
                {
                    if(temphigh > cell_array[i+1][j].altitudes)
                    {
                        temphigh=cell_array[i+1][j].altitudes;
                        cell_array[i][j].direction=5;
                    }
                }
                if(temphigh==cell_array[i][j].altitudes)
                {
                    cell_array[i][j].direction=1;
                }

            }
        }
     int m,n;
     cout<<"Case #"<<T-numT<<":"<<endl;
     for(int i=0 ; i<H; i++)
        for(int j=0; j<W; j++)
        {
            m=i;
            n=j;
		//	if(cell_array[m][n].basin==0)
			//	cell_array[m][n].basin=nowget++;
		//	{
		//	}
			char basinthis;
			basinthis;
			if(i==0&&j==0);
			else if (cell_array[m][n].basin==0)
				cell_array[m][n].basin=nowget++;


			basinthis=cell_array[m][n].basin;
			mymn.i=m;
			mymn.j=n;
			ijpair.push(mymn);

            while(cell_array[m][n].direction!=1)
            {
				//basinthis=cell_array[m][n].basin;

                 if(cell_array[m][n].direction==2)
                 {
					 if(cell_array[m-1][n].basin==0)
                     {
						 cell_array[m-1][n].basin=cell_array[m][n].basin;
						 m=m-1;
					 }
					 else
					 {
						 m=m-1;
						 break;
					 }

                 }
                if(cell_array[m][n].direction==3)
                 {
					if(cell_array[m][n-1].basin==0)
					{
						cell_array[m][n-1].basin=cell_array[m][n].basin;
						n=n-1;
					}
					else
					{
						n=n-1;
						break;
					}
                 }
                 if(cell_array[m][n].direction==4)
                 {
                     if( cell_array[m][n+1].basin==0)
					 {
						 cell_array[m][n+1].basin=cell_array[m][n].basin;
						 n=n+1;
					 }
					 else
					 {
						 n=n+1;
						 break;
					 }

                 }
                 if(cell_array[m][n].direction==5)
                 {
					 if(cell_array[m+1][n].basin==0)
                     {
						 cell_array[m+1][n].basin=cell_array[m][n].basin;
						m=m+1;
					 }
					 else
					 {
						 m=m+1;
						 break;
					 }
                 }
				 mymn.i=m;
				mymn.j=n;
			    ijpair.push(mymn);
            }
			if(cell_array[m][n].basin==basinthis);

			else
			{
				while(!ijpair.empty())
				{
					mymn=ijpair.top();
					cell_array[mymn.i][mymn.j].basin=cell_array[m][n].basin;
					ijpair.pop();
				}
				nowget--;
			}
			while(!ijpair.empty())
				ijpair.pop();



           cout << cell_array[i][j].basin<<" ";
		   if(j==W-1)
		   cout <<endl;
        }


    }


	return 0;
}

