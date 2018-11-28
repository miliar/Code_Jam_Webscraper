#include<fstream.h>
#include<iostream.h>
#include<conio.h>
#include<string.h>
#include<stdlib.h>

//using namespace std;

int main ()
{
  unsigned char buffer[25600];
  int recordcount=0,record=0;
  clrscr();
  ifstream myfile ("d:\\test\\A-small.in");
  //ifstream myfile ("d:\\test\\small1.txt");
  ofstream outputfile;
  outputfile.open("d:\\test\\opt.in");
  int k=0;
  while (! myfile.eof() )
  {

    if(k==0)
    {
     strcpy(buffer," ");
     myfile.getline (buffer,200);
     record=atoi(buffer);
     cout<<record;
     k++;
    }
    else
    {
	for(recordcount=1;recordcount<=record;recordcount++)
	{
	  int enginecount=0,count=0,querycount=0;
	  int max=0,switchflag=0,flag=1,result=0,current=0;
	  char engines[101][60];
	  char query[101][60];

	  myfile.getline (buffer,200);
	  enginecount=atoi(buffer);
	  for(count=0;count<enginecount;count++)
	  {
		strcpy(buffer,"");
		myfile.getline (buffer,200);
		strcpy(engines[count],buffer);
	  }
	   strcpy(buffer,"");
	  myfile.getline (buffer,200);
	  querycount=atoi(buffer);
	  for(count=0;count<querycount;count++)
	  {
	       strcpy(buffer,"");
		myfile.getline (buffer,200);
		strcpy(query[count],buffer);
	  }

	 while(flag!=0)
	 {
		for(int i=0;i<enginecount;i++)
		{
		  result=0;

		  for(int j=max;j<querycount;j++)
		  {

			if(strcmp(engines[i],query[j])==0)
			{
				result=1;
				if(current<=j)
				   current=j;break;

			}
		  }


			if(result==0)
			{
			      flag=0;

				
			}

		 }
		 max=current;

		switchflag++;

	 }

	 outputfile<<"Case #"<<recordcount<<": "<<switchflag-1<<endl;
	 if(recordcount==record)
	 {
	  outputfile.close();
	  return 0;
	 }

	}

    }
  }
  return 0;
}
