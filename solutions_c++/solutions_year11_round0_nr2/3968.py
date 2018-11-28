#include<stdio.h>
      int t,c,c_sto,d,d_sto,t_sto,n_sto,n;
	int temp1,temp2;
      char comb[36][3];
	char remv[28][2];
	char test[100];
	char answer[100];
	
	int length,track1,track2;
int check_combine(char a, char b)
{int i;
for (i=0;i<c_sto;i++)
{if (a==comb[i][0])
	{if (b==comb[i][1])
		{return i;
		    }
	}
 else {if (b==comb[i][0])
	{if (a==comb[i][1])
		{return i;
		    }
	}
	    }

}
return -1;
    }
int check_remv(char a,char b)
{int i;
for (i=0;i<d_sto;i++)
{if ((a==remv[i][0])&&(b==remv[i][1]))
return i;
else if ((b==remv[i][0])&&(a==remv[i][1]))
return i;
}
return -1;
}
main()
{FILE *f,*out;



f=fopen("input.txt","r");      
out=fopen("output.txt","w");      
fscanf(f,"%d",&t);
t_sto=t;
      while(t--)
      {fscanf(f,"%d",&c);
      c_sto=c;
      while(c--)
      {fscanf(f,"%s",comb[c_sto-c-1]);
         }
	fscanf(f,"%d",&d);
	d_sto=d;
	while (d--)
        {fscanf(f,"%s",remv[d_sto-d-1]);
	}
	fscanf(f,"%d",&n);
	n_sto=n;
	fscanf(f,"%s",test);
	fprintf(out,"Case #%d: [",t_sto-t);
	track1=0;
	track2=0;
	answer[0]=test[0];
	while(track1<n_sto)
	{	track1++;	track2++;
		answer[track2]=test[track1];
	temp1=check_combine(answer[track2],answer[track2-1]);
		if (temp1!=-1) {answer[track2-1]=comb[temp1][2];
			track2--;
			}
	else {for (temp1=0;temp1<track2;temp1++)
	{temp2=check_remv(answer[temp1],answer[track2]);
	    if (temp2!=-1){track2=-1;}
	}}	

	}	
	temp2=0;if (track2>0){
	while(1)
	{if (temp2<track2-1)
	fprintf(out,"%c, ",answer[temp2++]);
	else {fprintf(out,"%c]\n",answer[temp2++]);break;}
	}	
        	}
else	fprintf(out,"]\n");
	}
      }
