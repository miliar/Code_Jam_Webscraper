#include <iostream>

using namespace std;
int nameUsed=0;
int map[100][100][2];
  int note,hight,width;

bool isValid(int x,int y)
{
  if (x>=0 && x<hight && y>=0 && y<width)
    {
      //  cout<<"valid "<<x<<" "<<y<<endl;
      return true;
    }
    else 
      {
	//	cout<<"invalid.."<<x<<"  "<<y<<endl;
	return false;
      }

}

void moveTo(int &x, int &y)
{
  //   cout<<"from  " <<x<<"  "<<y <<"   to  ";
	bool flag=false;
  int tx=x,ty=y,min=map[x][y][0];
   if(isValid(x+1,y) && (map[x+1][y][0]<min || (map[x+1][y][0]==min && flag)))
    {
      tx=x+1;
      ty=y;
      min=map[tx][ty][0];
	flag=true;
    }
  if(isValid(x,y+1) && (map[x][y+1][0]<min || (map[x][y+1][0]==min && flag)))
    {
      tx=x;
      ty=y+1;
      min=map[tx][ty][0];
flag=true;
    }
if(isValid(x,y-1) && (map[x][y-1][0]<=min || (map[x][y-1][0]==min && flag)))
    {
      tx=x;
      ty=y-1;
      min=map[x][y-1][0];
flag=true;
    }
  
  if(isValid(x-1,y) && (map[x-1][y][0]< min || (map[x-1][y][0]==min && flag)))
    {
      tx=x-1;
      ty=y;
      min=map[tx][ty][0];
flag=true;
    }
  
  x=tx;
  y=ty;
  //cout<<x<<"  "<<y<<endl;
}




char name(int x, int y)
{
  int tx=x,ty=y;
  if(map[x][y][1]!=0)
    return map[x][y][1];

  moveTo(tx,ty);
  if(tx==x&&ty==y && map[x][y][1]==0)
    {
      //   cout<<"new name used at "<<x <<"  "<<y<<endl;
      map[x][y][1]='a'+nameUsed;
      nameUsed++;
      return map[x][y][1];
    }
  else
    {
      map[x][y][1]=name(tx,ty);      
      return map[x][y][1];
    }    
  
}



int main()
{

  int i;
  cin>>note;
  for( i=0;i<note;i++)
    {
      nameUsed=0;
      cin>>hight>>width;
      for(int j=0;j<hight;j++)
	{
	  for(int k=0;k<width;k++)
	    {
	      cin>>map[j][k][0];
	      map[j][k][1]=0;
	    }
	}
    
  for(int j=0;j<hight;j++)
    {
      for(int k=0;k<width;k++)
	name(j,k);
    }
  cout<<"Case #"<<i+1<<":"<<endl;
  for(int k=0;k<hight;k++)
    {
      for(int j=0;j<width;j++)
	{
	  cout<<(char)map[k][j][1];
	  if(j!=width-1) cout<<" ";
	}
      cout<<endl;
    }
    }
    
}
