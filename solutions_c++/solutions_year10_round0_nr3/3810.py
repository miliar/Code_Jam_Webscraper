#include<iostream.h>
#include<conio.h>
#include<string.h>
#include<stdio.h>
#include<math.h>
#include<fstream.h>
#define ROW 1000


ifstream fpi_in;

class roller
{
	private:
		unsigned long r,k,sum,s,ctr,ptr,i,arr[ROW],pos,money;
		int n,count;
	public:
		/*void arr_init()
		{
			for(int ki=0;ki<ROW;ki++)
			{
				//arr[k][0]=0;
				arr[ki][1]=0;
			}
		}*/
		void init()
		{
			//cout<<"hello\n";
			money=0;
			r=0;
			k=0;
			n=0;
			sum=0;
			s=0;
			ctr=0;
			pos=0;
			count=0;
			for(int ki=0;ki<ROW;ki++)
			{
				arr[ki];
		//		arr[ki][1]=0;
			}
		}
		void input()
		{
			char temp[2];
			fpi_in.getline(temp,2,'\n');
			fpi_in>>r;
			//cout<<"R="<<r<<endl;
			//getch();
			fpi_in>>k;
			//cout<<"k="<<k<<endl;
			fpi_in>>n;
			//cout<<"n="<<n<<endl;
			fpi_in.getline(temp,2,'\n');
			for(int ct=0;ct<n;ct++)
			{
				fpi_in>>arr[ct];//[0];
				//cout<<" "<<arr[ct][0];
			}
			
		}
		unsigned long calc()
		{
			//unsigned long position;
			//position=0;
			money=0;
			pos=-1;
			for(i=0;i<r;i++)
			{
				sum=0;
				s=0;
				count=0;
				//pos=-1;
				while(s<=k)
				{
					pos++;
					pos=pos%n;
					sum=s;
					//if(arr[pos][1]==1)
					if(count>=n)
						break;
					//else//{
					s=s+arr[pos];//[0];
					count++;
						//arr[pos][1]=1;
					//}
				}
				pos--;
				/*pos=pos%n;
				if(pos<0)
					pos=0-pos;*/
				cout<<"hello";
				money=money+sum;
				//arr_init();
			}
			//cout<<"money: "<<money<<endl;
			return money;
		}
};

void main()
{
	//clrscr();
	//cout<<"tryi="<<(-10%8);
	fstream fpo_out;
	fpo_out.open("c_o.txt",ios::out,ios::in);
	int t;
	t=0;
	unsigned long money;
	money=0;
	//location of input file (need this name only)
	fpi_in.open("c_small.in");
	fpi_in>>t;
	//cout<<"T="<<t<<endl;
	//getch();
	roller obj;
	for(int i=0;i<t;i++)
	{
		money=0;
		obj.init();
		obj.input();
		//obj.calc();
		money=obj.calc();
		fpo_out<<"Case #"<<i+1<<": "<<money<<endl;
	}
	fpo_out.close();
	fpi_in.close();
}
