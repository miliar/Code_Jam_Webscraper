#include<cstdio>

#define MAX_B 100001

using namespace std;

float typed[MAX_B];
float pb[MAX_B];

int main()
{
  int t, a, b;
  float kt, pe, min, ps, pg;
  FILE *inp, * out;
  inp = fopen("input.txt","r");
  out = fopen("output.txt","w");
  fscanf(inp,"%d",&t);
  for (int k=0; k<t; k++)
  {
    fscanf(inp,"%d %d",&a,&b);
    for (int i=0; i<a; i++)
      fscanf(inp,"%f",&typed[i]);
    pg = 1;
    kt = 0;
    pe = 0;
    for (int i=0; i<=a; i++)
      pb[i] = 0;
    for (int i=0; i<a; i++)
    {
      //printf("Posizione %d\n",i);
      ps = pg * (1-typed[i]);
      //printf("Probabilita di sbaglliare %f\n",ps);
      kt += ps * (b-a+1+b+1);
      //printf("Keep typing: %d\n",b-a+1+b+1);
      //printf("kt %f\n",kt);
      pe += ps * (1+b+1);
      //printf("Press enter: %d\n",1+b+1);
      //printf("pe %f\n",pe);
      for (int j=1; j<=a-i-1; j++)
      {
	pb[j] += ps * (2*j+b-a+1+b+1);
	//printf("Press backspace %d: %d\n",j,2*j+b-a+1+b+1);
	//printf("pb%d %f\n",j,pb[j]);
      }
      for (int j=a-i; j<= a; j++)
      {
	pb[j] += ps * (2*j+b-a+1);
	//printf("Press backspace %d: %d\n",j,2*j+b-a+1);
	//printf("pb%d %f\n",j,pb[j]);
      }
      pg = pg * typed[i];
    }
    //printf("Se giusto\n");
    //printf("Probabilita di fare giusto %f\n",pg);
    kt += pg * (b-a+1);
    //printf("Keep typing: %d\n",b-a+1);
    //printf("kt %f\n",kt);
    pe += pg * (1+b+1);
    //printf("Press enter: %d\n",1+b+1);
    //printf("pe %f\n",pe);
    for (int j=1; j<=a; j++)
    {
      pb[j] += pg * (2*j+b-a+1);
      //printf("Press backspace %d: %d\n",j,2*j+b-a+1);
      //printf("pb%d %f\n",j,pb[j]);
    }
    min = kt;
    if (pe < min)
      min = pe;
    for (int j=1; j<=a; j++)
      if (pb[j] < min)
	min = pb[j];
    fprintf(out,"Case #%d: %f\n",k+1,min);
  }
  fclose(inp);
  fclose(out);
  return 0;
}
