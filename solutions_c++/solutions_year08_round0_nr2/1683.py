#include<iostream.h>
#include<conio.h>
#include<string.h>
#include<stdio.h>
#include<math.h>
#include<fstream.h>
#define ROW 100

ifstream fp_in;

class train
{
	private:
		int na,nb,numa,numb,t;
		char tad[ROW][6],taa[ROW][6];
		char tbd[ROW][6],tba[ROW][6];
		int tad_hr[ROW],tad_min[ROW],taa_hr[ROW],taa_min[ROW];
		int tbd_hr[ROW],tbd_min[ROW],tba_hr[ROW],tba_min[ROW];
		int tad_tot[ROW],taa_tot[ROW],tbd_tot[ROW],tba_tot[ROW];
		int tad_tot1[ROW],taa_tot1[ROW],tbd_tot1[ROW],tba_tot1[ROW];
	public:
		void init()
		{
			int i,j;
			for(i=0;i<ROW;i++)
			{
				tad_hr[i]=0;
				tad_min[i]=0;
				taa_hr[i]=0;
				taa_min[i]=0;
				tbd_hr[i]=0;
				tbd_min[i]=0;
				tba_hr[i]=0;
				tba_min[i]=0;

				tad_tot[i]=0;
				taa_tot[i]=0;
				tbd_tot[i]=0;
				tba_tot[i]=0;
				tad_tot1[i]=0;
				taa_tot1[i]=0;
				tbd_tot1[i]=0;
				tba_tot1[i]=0;
				for(j=0;j<5;j++)
				{
					tad[i][j]=NULL;
					taa[i][j]=NULL;
					tbd[i][j]=NULL;
					tba[i][j]=NULL;
				}
			}
			na=0;
			nb=0;
			numa=0;
			numb=0;
			t=0;
		}

		void input_t()
		{
			fp_in>>t;
			//cout<<"\nt: "<<t;
		}

		void input_a()
		{
			fp_in>>na;
		//	cout<<"na: "<<na;
		//	getch();
			fp_in>>nb;
			//cout<<"nb: "<<nb<<endl;
		//	getch();
			int i,j,getn;
			char temp1[2];
			char temp[10];
			fp_in.getline(temp1,2,'\n');
			for(i=0;i<na;i++)
			{
				fp_in>>temp;
				strcpy(tad[i],temp);
				fp_in>>temp;
				strcpy(taa[i],temp);

				getn=tad[i][0];
				tad_hr[i]=(getn-48)*10;
				getn=tad[i][1];
				tad_hr[i]+=(getn-48);
				
				getn=tad[i][3];
				tad_min[i]=(getn-48)*10;
				getn=tad[i][4];
				tad_min[i]+=(getn-48);


				getn=taa[i][0];
				taa_hr[i]=(getn-48)*10;
				getn=taa[i][1];
				taa_hr[i]+=(getn-48);
				
				getn=taa[i][3];
				taa_min[i]=(getn-48)*10;
				getn=taa[i][4];
				taa_min[i]+=(getn-48);

				taa_tot[i]=taa_hr[i]*60+taa_min[i];
				taa_tot1[i]=taa_tot[i];
				tad_tot[i]=tad_hr[i]*60+tad_min[i];
				tad_tot1[i]=tad_tot[i];
			}
			
			for(i=0;i<na-1;i++)
			{
				for(j=i+1;j<na;j++)
				{
					if(taa_tot[i]>taa_tot[j])
					{
						getn=taa_tot[i];
						taa_tot[i]=taa_tot[j];
						taa_tot[j]=getn;

						getn=tad_tot[i];
						tad_tot[i]=tad_tot[j];
						tad_tot[j]=getn;
					}
					if(tad_tot1[i]>tad_tot1[j])
					{
						getn=tad_tot1[i];
						tad_tot1[i]=tad_tot1[j];
						tad_tot1[j]=getn;

						getn=taa_tot1[i];
						taa_tot1[i]=taa_tot1[j];
						taa_tot1[j]=getn;
					}
				}
			}

			for(i=0;i<nb;i++)
			{
				fp_in>>temp;
				strcpy(tbd[i],temp);
				fp_in>>temp;
				strcpy(tba[i],temp);

				getn=tbd[i][0];
				tbd_hr[i]=(getn-48)*10;
				getn=tbd[i][1];
				tbd_hr[i]+=(getn-48);
				
				getn=tbd[i][3];
				tbd_min[i]=(getn-48)*10;
				getn=tbd[i][4];
				tbd_min[i]+=(getn-48);

				getn=tba[i][0];
				tba_hr[i]=(getn-48)*10;
				getn=tba[i][1];
				tba_hr[i]+=(getn-48);
				
				getn=tba[i][3];
				tba_min[i]=(getn-48)*10;
				getn=tba[i][4];
				tba_min[i]+=(getn-48);

				tba_tot[i]=tba_hr[i]*60+tba_min[i];
				tba_tot1[i]=tba_tot[i];
				tbd_tot[i]=tbd_hr[i]*60+tbd_min[i];
				tbd_tot1[i]=tbd_tot[i];
			}
			

			for(i=0;i<nb-1;i++)
			{
				for(j=i+1;j<nb;j++)
				{
					if(tba_tot[i]>tba_tot[j])
					{
						getn=tba_tot[i];
						tba_tot[i]=tba_tot[j];
						tba_tot[j]=getn;

						getn=tbd_tot[i];
						tbd_tot[i]=tbd_tot[j];
						tbd_tot[j]=getn;
					}
					if(tbd_tot1[i]>tbd_tot1[j])
					{
						getn=tbd_tot1[i];
						tbd_tot1[i]=tbd_tot1[j];
						tbd_tot1[j]=getn;

						getn=tba_tot1[i];
						tba_tot1[i]=tba_tot1[j];
						tba_tot1[j]=getn;
					}
				}
			}

			if(na>nb)
			{
				for(i=nb;i<na;i++)
					tba_tot[i]=24*60+1;
			}
			else
			{
				for(i=na;i<nb;i++)
					taa_tot[i]=24*60+1;
			}

		}

		void calc()
		{
		    int i,j,k; 
			i=0;
			for(j=0;j<nb;j++)
			{
				if((taa_tot[i]+t)>tbd_tot1[j])
					numb++;
				else
				{
					i++;
				//	if(i==na)
				//		break;
				}
			}
			i=0;
			for(j=0;j<na;j++)
			{
				if((tba_tot[i]+t)>tad_tot1[j])
					numa++;
				else
				{
					i++;
				//	if(i==nb)
				//		break;
				}
			}

		}

		int ret_a()
		{
			return(numa);
		}

		int ret_b()
		{
			return(numb);
		}

};


void main()
{
	//clrscr();
	fstream fp_out;
	fp_out.open("train.txt",ios::out,ios::in);
	int n,i,numa=0,numb=0;
	//location of input file (need this name only)
	fp_in.open("b1.in");
	fp_in>>n;
	//cout<<"N: "<<n;
	train obj;
	for(i=0;i<n;i++)
	{        
		obj.init();
		obj.input_t();
		obj.input_a();
		obj.calc();
		numa=obj.ret_a();
		numb=obj.ret_b();

		fp_out<<"Case #"<<i+1<<": "<<numa<<" "<<numb<<endl;
	}
	fp_out.close();
	fp_in.close();
}