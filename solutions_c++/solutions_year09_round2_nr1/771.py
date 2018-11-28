// CodeJam-20090912-1.cpp : Defines the entry point for the console application.
//

#define _CRT_SECURE_NO_WARNINGS

#include <string>
#include <map>

using namespace std;

struct Tree
{
   Tree(Tree *pPar)
   {
      dblWeight = 0.0;
      pParent   = pPar;
      pTreeYes  = NULL;
      pTreeNo   = NULL;
   }

   double
      dblWeight;

   string
      strFeature;

   Tree
      *pParent,
      *pTreeYes,
      *pTreeNo;
};

void read_tree(Tree *pCurr, FILE *fpi)
{
   char
      cNext,
      szBuf[100];

   while (pCurr->dblWeight == 0.0)
   {
      fscanf(fpi, "%s", szBuf);
      sscanf(szBuf, "%lf", &pCurr->dblWeight);

      if (pCurr->dblWeight == 0.0)
         sscanf(szBuf + 1, "%lf", &pCurr->dblWeight);
   }

   fscanf(fpi, "%c", &cNext);

   if (cNext == ')' || cNext == '\n')
      return;
   else
   {
      fscanf(fpi, "%s", &szBuf);

      if (szBuf[0] == ')')
         return;

      pCurr->strFeature = szBuf;
      pCurr->pTreeYes   = new Tree(pCurr);
      pCurr->pTreeNo    = new Tree(pCurr);
      read_tree(pCurr->pTreeYes, fpi);
      read_tree(pCurr->pTreeNo, fpi);
   }
}

double compute_probability(Tree *pCurr, double prob, map<string, int> mapFeatures)
{
   if (pCurr)
   {
      prob *= pCurr->dblWeight;
      if (mapFeatures.find(pCurr->strFeature) != mapFeatures.end())
         return compute_probability(pCurr->pTreeYes, prob, mapFeatures);

      return compute_probability(pCurr->pTreeNo, prob, mapFeatures);
   }

   return (prob);
}

int main(int argc, char * argv[])
{
	FILE
		*fpi = fopen("A-large.in", "r"),
		*fpo = fopen("A-large.out", "w");

	int
		N,
      L,
      A,
      n;

   char
      szBuf[100],
      szAnimal[100],
      szFeature[100];

   fscanf(fpi, "%d", &N);
   for (int i = 0; i < N; i++)
   {
      fprintf(fpo, "Case #%d:\n", i + 1);

      fscanf(fpi, "%d", &L);

      Tree
         *pRoot = new Tree(NULL);

      read_tree(pRoot, fpi);

      A = 0;
      while (A == 0)
      {
         fscanf(fpi, "%s", szBuf);
         sscanf(szBuf, "%d", &A);
      }

      for (int j = 0; j < A; j++)
      {
         fscanf(fpi, "%s", szAnimal);
         fscanf(fpi, "%d", &n);

         map<string, int>
            mapFeatures;

         for (int k = 0; k < n; k++)
         {
            fscanf(fpi, "%s", szFeature);
            mapFeatures[szFeature] = 0;
         }

         fprintf(fpo, "%.7lf\n", compute_probability(pRoot, 1.0, mapFeatures));
      }
   }
}
