#include <iostream>
#include <fstream>

using namespace std;

int najnizej(int n, int s, int e, int w)
{
  if ( n<=s && n<=e && n<=w )
    return n;
  if ( s<=n && s<=e && s<=w )
    return s;
  if ( e<=s && e<=n && e<=w )
    return e;
  if ( w<=s && w<=e && w<=n )
    return w;
}

int main()
{
  ofstream f_output("output");
  ifstream f_input("input");
  string x;
  int H, W;
  int n,w,e,s;
  int index = 1;
  int arr[102][102];
  int tmp[101][101];
  char wyn[101][101];
  char chs[] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
  int a;
  int ilosc_terenow;
  f_input >> ilosc_terenow;
  for (int p=1; p<=ilosc_terenow; p++)
    {
      //zerowanie
      for (int i=0; i<=102; i++)
	{
	  for (int j=0; j<=102; j++)
	    {
	      arr[i][j] = 0;
	      tmp[i][j] = 0;
	      //wyn[i][j] = ;
	    }
	}

      //zerowanie

      f_input >> H;
      f_input >> W;
      for (int i=0; i<=101; i++)
	{
	  for (int j=0; j<=101; j++)
	    {
	      arr[i][j] = 11111;
	    }
	}
      for (int i=1; i<=H; i++)
	{
	  for (int j=1; j<=W; j++)
	    {
	      f_input >> a;
	      arr[i][j] = a;
	    }
	}
      for (int i=1; i<=H; i++)
	{
	  for (int j=1; j<=W; j++)
	    {
	      if (! tmp[i][j] )
		{
		  tmp[i][j]=index++;
		  //cout << "!" << tmp[i][j] << " " << index << endl;
		}
	  
	      n=arr[i-1][j]; s=arr[i+1][j]; e=arr[i][j+1]; w=arr[i][j-1];
	      //cout << "nsew" << n << s << e << w << endl;
	      //cout << najnizej(n,s,e,w) << endl;
	      if ( arr[i][j] > najnizej(n,s,e,w) )
		{
		  if (n == najnizej(n,s,e,w) )
		    {
		      if ( tmp[i-1][j] )
			{
			  // zamien_w_tabeli( tmp[][], tmp[i-1][j], tmp[i][j], H, W);
			  int do_zamiany = tmp[i-1][j];
			  for (int k=1; k<=H; k++)
			    {
			      for (int l=1; l<=W; l++)
				{
				  if ( tmp[k][l] ==  do_zamiany )
				    tmp[k][l] = tmp[i][j];
				}
			    }
			}
		      else
			tmp[i-1][j] = tmp[i][j];
		    }
		  else 
		    if (w == najnizej(n,s,e,w) )
		      // tmp[i][j-1] = tmp[i][j];
		      {
			if ( tmp[i][j-1] )
			  {
			    // zamien_w_tabeli( tmp[][], tmp[i][j-1], tmp[i][j], H, W);
			    int do_zamiany = tmp[i][j-1];
			    for (int k=1; k<=H; k++)
			      {
				for (int l=1; l<=W; l++)
				  {
				    if ( tmp[k][l] ==  do_zamiany )
				      tmp[k][l] = tmp[i][j];
				  }
			      }
			  }
			else
			  tmp[i][j-1] = tmp[i][j];
		      }
		    else 
		      if (e == najnizej(n,s,e,w) )
			//tmp[i][j+1] = tmp[i][j];
			{
			  if ( tmp[i][j+1] )
			    {
			      // zamien_w_tabeli( tmp[][], tmp[i][j+1], tmp[i][j], H, W);
			      int do_zamiany = tmp[i][j+1];
			      for (int k=1; k<=H; k++)
				{
				  for (int l=1; l<=W; l++)
				    {
				      if ( tmp[k][l] == do_zamiany )
					tmp[k][l] = tmp[i][j];
				    }
				}
			    }
			  else
			    tmp[i][j+1] = tmp[i][j];
			}
		      else 
			if (s == najnizej(n,s,e,w) )
			  //tmp[i+1][j] = tmp[i][j];
			  {
			    if ( tmp[i+1][j] )
			      {
				// zamien_w_tabeli( tmp[][], tmp[i+1][j], tmp[i][j], H, W);
				int do_zamiany = tmp[i+1][j];
				for (int k=1; k<=H; k++)
				  {
				    for (int l=1; l<=W; l++)
				      {
					if ( tmp[k][l] ==  do_zamiany )
					  tmp[k][l] = tmp[i][j];
				      }
				  }
			      }
			    else
			      tmp[i+1][j] = tmp[i][j];
			  }
		}
	      else
		{
		  //	  cout << "asaaaaaaaa" << arr[i][j] << endl;
		  int poprzednie = tmp[i][j];
		  tmp[i][j]=index++;
		  for (int k=1; k<=H; k++)
		    {
		      for (int l=1; l<=W; l++)
			{
			  if ( tmp[k][l] == poprzednie )
			    tmp[k][l] = tmp[i][j];
			}
		    }
		}



	      /*    cout << "~~~~~~~~~~" << endl;
	      for (int i=1; i<=H; i++)
		{
		  for (int j=1; j<=W; j++)
		    {
		      cout << tmp[i][j] << " ";
		    }
		  cout << endl;
		}
	      */



	    }
	}

      /*
      cout << endl;
      for (int i=1; i<=H; i++)
	{
	  for (int j=1; j<=W; j++)
	    {
	      cout << arr[i][j] << " ";
	    }
	  cout << endl;
	}
      cout << endl;
      for (int i=1; i<=H; i++)
	{
	  for (int j=1; j<=W; j++)
	    {
	      cout << tmp[i][j] << " ";
	    }
	  cout << endl;
	  }*/

      int q = 0;
      for (int i=1; i<=H; i++)
	{
	  for (int j=1; j<=W; j++)
	    {


	      if ( ! wyn[i][j] )
		{
		  wyn[i][j] = chs[q];
		  //cout << "q: " << chs[q] << endl;
		  q++;
		  for (int k=1; k<=H; k++)
		    {
		      for (int l=1; l<=W; l++)
			{
			  if (tmp[i][j] == tmp[k][l] )
			    {
			      wyn[k][l] = wyn[i][j];
			      //tmp[k][l] = 11111;
			    }
			}
		    }

		}


	    }
	}


      //cout << endl;
      f_output << "Case #" << p << ":" << endl;
      for (int i=1; i<=H; i++)
	{
	  for (int j=1; j<=W; j++)
	    {
	      f_output << wyn[i][j] << " ";
	    }
	  f_output << endl;
	}

    }
  return 0;
}
