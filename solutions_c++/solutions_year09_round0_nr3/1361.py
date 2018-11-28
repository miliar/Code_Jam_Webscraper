#include <iostream>
#include <string.h>

using namespace std;
char input[502],comto[20]="welcome to code jam";
int **letterPos[20];
int len;


void init()
{
    
  for(int i=0;i<=19;i++)
    {
      //  cout<<i<<endl;
      letterPos[i]=new int*[500];
      if(letterPos[i]==NULL)
	cout<<"memory full"<<endl;
      for(int j=0;j<500;j++)
	{
	  letterPos[i][j]=new int[2];
	}
      letterPos[i][0][0]=0;                     //first number represend the number of numbers in.
    }
    
}



int process(int from ,int forWhat)
{
  int oc;
  long int count=0;
  if(from>=len )
    return 0;
  else if(forWhat==19)
    return 1;

  for(oc=1;oc<=letterPos[forWhat][0][0];oc++)
    {
      if(letterPos[forWhat][oc][0]>=from)
	break;
    }
  for(oc=oc;oc<=letterPos[forWhat][0][0];oc++)
    {
      if(letterPos[forWhat][oc][1]<0)
	letterPos[forWhat][oc][1]=process(letterPos[forWhat][oc][0],forWhat+1);
      count+=letterPos[forWhat][oc][1];      
    }
  //cout<<" from ="<<from <<"  fromWhat = "<<comto[forWhat]<<endl;
  return count%10000;
  
}


void print()
{
  for(int i=0;i<=18;i++)
    {
      cout<<comto[i]<<"  ";
      for(int j=0;j<=letterPos[i][0][0];j++)
	{
	  cout<<letterPos[i][j][0]<<" "<<letterPos[i][j][1]<<"  ";
	}
	    cout<<endl;
    }
}

void processInput()
{
  for(int i=0;i<len;i++)
    {
      //cout<<"processing ... "<<input[len]<<endl;
      switch(input[i])
	{
	case 'w': letterPos[0][0][0]++;
	  letterPos[0][letterPos[0][0][0]][0]=i;
	  letterPos[0][letterPos[0][0][0]][1]=-1;
	  break;
	case 'e': letterPos[1][0][0]++;
	  letterPos[1][letterPos[1][0][0]][0]=i;
	  letterPos[1][letterPos[1][0][0]][1]=-1;
	   letterPos[6][0][0]++;
	  letterPos[6][letterPos[6][0][0]][0]=i;
	  letterPos[6][letterPos[6][0][0]][1]=-1;
	   letterPos[14][0][0]++;
	  letterPos[14][letterPos[14][0][0]][0]=i;
	  letterPos[14][letterPos[14][0][0]][1]=-1;
	  break;
	case 'l': letterPos[2][0][0]++;
	  letterPos[2][letterPos[2][0][0]][0]=i;
	  letterPos[2][letterPos[2][0][0]][1]=-1;
	  break;
	case 'c': letterPos[3][0][0]++;
	  letterPos[3][letterPos[3][0][0]][0]=i;
	  letterPos[3][letterPos[3][0][0]][1]=-1;
	   letterPos[11][0][0]++;
	  letterPos[11][letterPos[11][0][0]][0]=i;
	  letterPos[11][letterPos[11][0][0]][1]=-1;
	  break;
	case 'o': letterPos[4][0][0]++;
	  letterPos[4][letterPos[4][0][0]][0]=i;
	  letterPos[4][letterPos[4][0][0]][1]=-1;
	   letterPos[9][0][0]++;
	  letterPos[9][letterPos[9][0][0]][0]=i;
	  letterPos[9][letterPos[9][0][0]][1]=-1;
	   letterPos[12][0][0]++;
	  letterPos[12][letterPos[12][0][0]][0]=i;
	  letterPos[12][letterPos[12][0][0]][1]=-1;
	  break;
	case 'm': letterPos[5][0][0]++;
	  letterPos[5][letterPos[5][0][0]][0]=i;
	  letterPos[5][letterPos[5][0][0]][1]=-1;
	   letterPos[18][0][0]++;
	  letterPos[18][letterPos[18][0][0]][0]=i;
	  letterPos[18][letterPos[18][0][0]][1]=-1;
	  break;
	case ' ': letterPos[7][0][0]++;
	  letterPos[7][letterPos[7][0][0]][0]=i;
	  letterPos[7][letterPos[7][0][0]][1]=-1;
	  letterPos[10][0][0]++;
	  letterPos[10][letterPos[10][0][0]][0]=i;
	  letterPos[10][letterPos[10][0][0]][1]=-1;
	   letterPos[15][0][0]++;
	  letterPos[15][letterPos[15][0][0]][0]=i;
	  letterPos[15][letterPos[15][0][0]][1]=-1;	   	  
	  break;
	case 't': letterPos[8][0][0]++;
	  letterPos[8][letterPos[8][0][0]][0]=i;
	  letterPos[8][letterPos[8][0][0]][1]=-1;
	  break;
	case 'd': letterPos[13][0][0]++;
	  letterPos[13][letterPos[13][0][0]][0]=i;
	  letterPos[13][letterPos[13][0][0]][1]=-1;
	  break;
	case 'j': letterPos[16][0][0]++;
	  letterPos[16][letterPos[16][0][0]][0]=i;
	  letterPos[16][letterPos[16][0][0]][1]=-1;
	  break;
	case 'a': letterPos[17][0][0]++;
	  letterPos[17][letterPos[17][0][0]][0]=i;
	  letterPos[17][letterPos[17][0][0]][1]=-1;
	  break;
    default:
       letterPos[19][0][0]++;
	  letterPos[19][letterPos[19][0][0]][0]=i;
	  letterPos[19][letterPos[19][0][0]][1]=-1;
	  break;
      

	
	}
    }
}


int getIndex(char a)
{
  switch(a)
    {
    case 'w': return 0;
      break;
    case'e': return 1;
      break;
    case 'l': return 2;
      break;
  case 'c': return 3;
      break;
    case'o': return 4;
      break;
    case 'm': return 5;
      break;
  case ' ': return 7;
      break;
    case't': return 8;
      break;
    case 'd': return 13;
      break;
  case 'j': return 16;
      break;
    case'a': return 17;
      break;
    default:
      return 19;
    }
}










int main()
{

  int n,i,index,temp;
  unsigned long int result;
  char outpu[5];
  init();
  cin>>n;

  for(i=1;i<=n;i++)
    {
      len=0;
      while(len==0)
      {
         cin.getline(input,501);
         len=strlen(input);
      }
      for(int j=0;j<=19;j++)
	letterPos[j][0][0]=0;
      
      processInput();
      //print();
      cout<<"Case #"<<i<<": ";
      outpu[4]='\0';
      result=process(0,0);
      
    for(int t=3;t>=0;t--)
    {
        outpu[t]=result%10 + '0';
        result/=10;
    }
    cout<<outpu<<endl;
    }


}
