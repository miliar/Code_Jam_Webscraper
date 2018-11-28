#include<fstream.h>
#include<string.h>
struct nod1 {char cuvp[16]; nod1 *urm;};
struct nod2 {char cuvt[500]; int nr; nod2 *urm;};

nod1 *prim; nod2 *prim2;

fstream f("A-small-attempt3(2).in", ios::in);
fstream g("date.out", ios::out);

 int L, D, N;

void citire (nod1 *&prim, nod2 *&prim2)
 {f>>L>>D>>N;

  nod1 *p, *ultim;
  char protip[500];
  f>>protip;
  prim=new nod1;
  strcpy (prim->cuvp, protip);
  prim->urm=NULL;
  ultim=prim;
  f>>protip;
  for (int i=2; i<=D; i++)
     {p=new nod1;
      strcpy (p->cuvp, protip);
      p->urm=NULL;
      ultim->urm=p;
      ultim=p;
      f>>protip;
      }

  nod2 *p2, *ultim2;
  char protip2[500];
  strcpy (protip2, protip);
  prim2=new nod2;
  strcpy (prim2->cuvt, protip2);
  prim2->nr=0;
  prim2->urm=NULL;
  ultim2=prim2;
  f>>protip2;
  for (int i=2; i<=N; i++)
     {p2=new nod2;
      strcpy (p2->cuvt, protip2);
      p2->nr=0;
      p2->urm=NULL;
      ultim2->urm=p2;
      ultim2=p2;
      f>>protip2;
      }

  }


void afisare2(nod2 *prim2)
 {nod2 *p;
  p=prim2;
  int i=1;
  while (p!=NULL)
   {g<<"Case #"<<i<<": "<<p->nr<<endl;
    p=p->urm;
    i++;
    }
  g.close();
  }

int match(char s[500], char c[500])
{int t=0, result=0, i, var;
 while (t<strlen(s))
   {
    if (s[t]=='(')
	    {
	    t++; var=0;
	    while(s[t]!=')')
		      {
		      if (s[t]==c[result]) {var++;}
		      t++;
		      }
	    if (var) result++;
	    t++;
	    }

    else if (s[t]==c[result])
		 {
		 t++; result++;
		 }
	 else break;

    }

 if(result==strlen(c)) return 1;
 else return 0;

 }

void decript (nod1 *prim, nod2 *prim2)
 {
  nod1 *p; nod2 *q;
  p=prim;
  while (p!=NULL)
   {q=prim2;
    while (q!=NULL) {if (match(q->cuvt, p->cuvp)) q->nr++;
		     q=q->urm;}
    p=p->urm;
   }

  }

void main()
{
 citire(prim, prim2);
 decript(prim, prim2);
 afisare2(prim2);


}
