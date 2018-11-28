#include <cstdio>
#include <string>
#include <vector>

using namespace std;

  vector<char> vect;
  
  void AddChar(char a)
  {
    if (vect.size() == 0)
    {
      vect.push_back(a);
      return;
    }
    for (int i=0; i<vect.size(); i++)
    {
      if (a < vect[i])
      {
	vect.push_back(a);
	for (int j = vect.size()-2; j>=i; j--)
	{
	  vect[j+1] = vect[j];
	}
	vect[i] = a;
	return;
      }
    }
    vect.push_back(a);
  }

int main()
{
int n = 0;
  FILE* in = fopen("in.in", "r");
  FILE* out = fopen("out.out", "w");
  fscanf(in,"%d\n", &n);
  char a;
  string str = "";

  for (int i=0; i<n; i++)
  {
    vect.clear();
    str = "0";
    while (true)
    {
      a = fgetc(in);
      if (a == EOF || a == '\n')
      {
	break;
      }
      str += a;
    }
    string res = "";
    if (str.size() > 0)
      
    for (int j=str.size() - 1; j>=0; j--)
    {
      if (vect.size() > 0)
      {
	
	
	if (str[j] < vect[vect.size() - 1])
	{	  
	  AddChar(str[j]);
	  for (int l=0; l<j; l++)
	  {
	    if (l != 0 || str[l] != '0')
	    {
	      res += str[l];
	    }
	  }
	  for (int l=0; l<vect.size() ; l++)
	  {
	    if (vect[l] > str[j])
	    {
	      res+=vect[l];
	      break;
	    }
	  }
	  //res += vect[vect.size() - 1];
	  bool flag = false;
	  for (int l = 0; l < vect.size(); l++)
	  {
	    if (vect[l] > str[j] && flag == false)
	    {
	      flag = true;
	      
	    }
	    else
	      res += vect[l];
	  }
	  fprintf(out, "Case #%d: ", i+1);
	  for (int q = 0; q<res.size(); q++)
	    fprintf(out, "%c", res[q]);
	  fprintf(out, "\n");
	  break;
	}
	else
	  AddChar(str[j]);

      }
      else
      {
	AddChar(str[j]);

      }
    }
  }
  fclose(in);
  fclose(out);
}