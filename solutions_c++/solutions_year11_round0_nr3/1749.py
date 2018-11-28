#include <iostream>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <algorithm>
#include <cmath>

using namespace std;

long correctpatval(long* sval, int index, int M);
long almostcorrect(long num1, long num2);
string convertInt(int number)
{
    if (number == 0)
        return "0";
    string temp="";
    string returnvalue="";
    while (number>0)
    {
        temp+=number%10+48;
        number/=10;
    }
    for (int i=0;i<temp.length();i++)
        returnvalue+=temp[temp.length()-i-1];
    return returnvalue;
}

//Sub function for quick sort algorithm
int partition(long* a, int left, int right)
{
  long pivot = a[left];
   while (true)
     {
       while (a[left] < pivot) left++;
       while (a[right] > pivot) right--;
       if (left > right)
	 {
	   std::swap(a[left], a[right]);
	 }
       else
	 {
	   return right;
	 }
     }
}


//Quick sort function
void quicksort(long* a, int left, int right)
{
  if (left < right)
    {
      int pivot = partition(a, left, right);
      quicksort(a, left, pivot-1);
      quicksort(a, pivot+1, right);
    }
}

void sortarray(int sdim, long* x)
{
  //descending order
  long temp = 0.0;  //holding variable
  long pivot = 0.0; //pivot variable

  for(int i = 0; i < sdim; i++)
    {
      //      pivot = x[i];
      for (int j=i+1; j < sdim; j++)
	{
	  if (x[j] < x[i])
	    { 
	      temp = x[i];             // swap elements
	      x[i] = x[j];
	      x[j] = temp;
	    }
	}
    }
}

int main(int argc, char** argv)
{
  int T, C, D, N, flen;
  ifstream input("C-large.in");
  ofstream output("C-large.out");
  long* cval;
  string result;
  long seanval, patval;
  int iter;

  input >> T;
  for(int i = 0; i < T; i++)
    {
      input >> N;
      cval = new long[N];
      for(int j = 0; j < N; j++)
	input >> cval[j];
            
      result = "NO";
      seanval = 0;
      patval = 0;
      iter = 0;

      if(N == 2)
	{
	  if(cval[0] == cval[1])
	    result = "YES";
	  seanval = cval[0];
	}
      else
	{
	  sortarray(N,cval);//,0,N-1);

	  for(int j = 1; j < N; j++)
	    seanval += cval[j];
	  patval = cval[0];
	  
	  while(iter < N-1)
	    {	      
	      if(correctpatval(cval,0,iter+1) == correctpatval(cval,iter+1,N))
		{
		  result = "YES";
		  break;
		}
	      else
		{
		  seanval = seanval - cval[iter+1];
		  patval = patval + cval[iter+1];
		  iter++; 
		}
	    }	  
	}
      
      if(result == "NO")
	output<<"Case #"<<i+1<<": "<<result<<endl;
      else
	{
	  if(seanval > patval)
	    output<<"Case #"<<i+1<<": "<<seanval<<endl;
	  else
	    output<<"Case #"<<i+1<<": "<<patval<<endl;
	}
      delete[] cval;
    }
  return 0;
}

long correctpatval(long* cval, int index, int M)
{
  int start = index;
  int finish = M;
  long cpatval;

  cpatval = cval[start];
  for(int j = start+1; j < finish; j++)
    cpatval = almostcorrect(cpatval, cval[j]);  
  return cpatval;
}

long almostcorrect(long num1, long num2)
{
  long correctval;
  string str1, str2, strfin;
  long bucket1, bucket2, bucketfin;
  int commonlen, str1len, str2len;
  
  bucket1 = num1;
  bucket2 = num2;

  if(bucket1 == bucket2)
    bucketfin = 0;
  else
    {
      str1 = "";
      while(bucket1 > 0)
	{
	  str1 = convertInt(bucket1%2) + str1;
	  bucket1 = bucket1 / 2;
	}      
      str2 = "";
      while(bucket2 > 0)
	{
	  str2 = convertInt(bucket2%2) + str2;
	  bucket2 = bucket2 / 2;
	}      
      
      if(str1 == "") 
	str1 = '0';
      if(str2 == "") 
	str2 = '0';
      
      str1len = str1.length();
      str2len = str2.length();
      commonlen = min(str1len, str2len);
      strfin = "";
      //patrick-type decimal
      for(int k = 0; k < commonlen; k++)
	{
	  if(str1[str1len-k-1] == '1' && str2[str2len-k-1] == '1')
 	    strfin = '0' + strfin;
	  else if(str1[str1len-k-1] == '0' && str2[str2len-k-1] == '0')
	    strfin = '0' + strfin;
	  else
	    strfin = '1'+ strfin;   
	}         
      
      if(commonlen == str2len)
	{
	  for(int k = str1len - commonlen - 1; k > -1; k--)
	    strfin = str1[k] + strfin;
	}
      else
	{
	  for(int k = str2len - commonlen -1; k > -1; k--)
	    strfin = str2[k] + strfin;	  
	}
      
      commonlen = strfin.length();
      bucketfin = 0;
      for(int k = 0; k < commonlen; k++)
	{
	  if(strfin[k] == '1')
	    bucketfin += pow(2,commonlen-k-1)*1;
	  else
	    bucketfin += pow(2,commonlen-k-1)*0;
	}
    }
  return bucketfin;
}


