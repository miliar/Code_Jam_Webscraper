#include<fstream.h>
#include<stdio.h>
#include<string.h>
#include<conio.h>


struct buttonpress
{
	char robot;
	int button;
};

int getnextbutton(buttonpress seq[],int n,int pos,char robot)
{
   for(int itr=pos;itr<=n;itr++)
   {
   if (seq[itr].robot == robot)
       return seq[itr].button;
   }
   return -1;
}

int getdirection(int cur,int pos)
{
   if (cur==pos)
   return 0;
   if (cur<pos)
   return 1;
   else
   return -1;
}


int process(buttonpress seq[],int n)
{
int o=1,b=1;
int second=0;
int nextobutton=-1,nextbbutton=-1;
int odirection,bdirection;
int iitrseq;

for(iitrseq=1;iitrseq<=n;iitrseq++)
{

 nextobutton=getnextbutton(seq,n,iitrseq,'O');
 nextbbutton=getnextbutton(seq,n,iitrseq,'B');



 odirection=getdirection(o,nextobutton);
 bdirection=getdirection(b,nextbbutton);

 if (seq[iitrseq].robot=='O')
 {

    while(odirection != 0)
    {

    printf("\no=%d b=%d od=%d bd=%d ob=%d bb=%d",o,b,odirection,bdirection,nextobutton,nextbbutton);


    o+=odirection;
    b+=bdirection;
    second++;


     odirection=getdirection(o,nextobutton);
     bdirection=getdirection(b,nextbbutton);



    }

    o+=odirection;
    b+=bdirection;
    second++;



 }
 else
 {
       while(odirection != 0)
    {
    o+=odirection;
    b+=bdirection;
    second++;


     odirection=getdirection(o,nextobutton);
     bdirection=getdirection(b,nextbbutton);



    }

    o+=odirection;
    b+=bdirection;
    second++;

 }




}

return second;

}

void main()
{
int inocase;
int inobutton;
int iitr;
buttonpress seq[101];

clrscr();

ifstream in;
in.open("input.in");
in>>inocase;
//cout<<"\n no case"<<inocase;
for(int iitrnocase=1;iitrnocase<=inocase;iitrnocase++)
{
in>>inobutton;


for( iitr=1;iitr<=inobutton;iitr++)

{
    in>>seq[iitr].robot>>seq[iitr].button;
}

cout<<"\n seq"<<inobutton;

for(iitr=1;iitr<=inobutton;iitr++)

{
  cout<<"\n"<<seq[iitr].robot<<" "<<seq[iitr].button;
}



cout<<"\n Case #"<<iitrnocase<<": "<<process(seq,inobutton);



}
in.close();
getch();
}