#include <iomanip>
#include <fstream>
#include <iostream>
using namespace std;
void sort(int array[],int zz,int yy)
	{
	int z,y,i,k;

	if(zz<yy)
		{
		z=zz;
		y=yy;
		k=array[z];

		do	{
				while((z<y)&&(array[y]>=k))
					y--;
					if(z<y)
						{
						array[z]=array[y];
						z=z+1;
						}
					while((z<y)&&(array[z])<=k)
						z++;
					if(z<y)
						{
						array[y]=array[z];
						}

			} while(z!=y);
		array[z]=k;
			sort(array,zz,z-1);
			sort(array,z+1,yy);
		}
	}

int main(){
    int i,j=0,n,m,x,y,s=0;
    int c[101]={0};
    ifstream fin("B-large.in",ios::in);
    ofstream fout("B-large.out",ios::out);
    fin>>n;
    while(n!=0)
    { fin >>m>>x>>y;s=0;
    for(i=0;i<m;i++)fin>>c[i];
    sort(c,0,m-1);
    for(i=m-1;i>=0;i--)
    {if(c[i]>=3*y-2){s++;}
     else if((y>1)&&(c[i]>=3*y-4)&&(x>0)){s++;x--;}
    }
    fout<<"Case #"<<++j<<": "<<s<<endl;
    n--;}
    fin.close();
    fout.close();
    return 0;
}
