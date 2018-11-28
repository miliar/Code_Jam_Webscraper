#include<fstream.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<conio.h>
#define MAX 80
struct eng
{ char name[MAX];
  int flag;
};

void main()
{ clrscr();
  ifstream fin("F:\\inputA.txt");
  ofstream fout("F:\\outputa.txt");
  int n;
  fin>>n;
  int i,j,k,switched=0,count;
  for(i=0;i<n;i++)
  { int s,q;
    switched=0;
    count=0;
    fin>>s;
    eng se[10];
    fin.getline(se[0].name,80);
    fflush(stdin);
    for(j=0;j<s;j++)
    { fin.getline(se[j].name,80);
      se[j].flag=0;
    }
    fin>>q;
    if(q==0)
    goto end;
    char query[100][MAX];
    fin.getline(query[0],80);
    char covered[10][MAX];

    count=0;
    for(j=0;j<q;j++)
      fin.getline(query[j],80);

    for(j=0;j<q;j++)
    {  for(k=0;k<s;k++)
	 { if(!strcmp(query[j],se[k].name)&&se[k].flag==0)
	    { se[k].flag=1;
	      count++;
	      break;
	    }
	 }
      if(count==s)
      { switched++;
	for(k=0;k<s;k++)
	{ se[k].flag=0;
	  if(!strcmp(query[j],se[k].name))
	  se[k].flag=1;
	}
	count=1;
      }
    }

    end:
    fout<<"Case #"<<i+1<<": "<<switched<<endl;
  }
  fin.close();
  fout.close();
}
