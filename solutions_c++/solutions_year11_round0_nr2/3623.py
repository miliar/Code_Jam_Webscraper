  #include "iostream.h"

  int T, N, C, D;
  char frnds[36][3];
  char enems[28][2];  

  char pair(char c1, char c2)
  {
    for (int i= 0; i<C ; i++)
    {
        if(frnds[i][0] == c1 && frnds[i][1] == c2)
          return frnds[i][2];
        if(frnds[i][0] == c2 && frnds[i][1] == c1)
          return frnds[i][2];
    }  
    return '\0';  
  }

  int opposed (char output[], int k, char elem)
  {
    for (int i= 0; i<k ; i++)
    {
      for (int j= 0; j<D ; j++)
      {
        if(enems[j][0] == output[i] && enems[j][1] == elem)
          return 1;
        if(enems[j][0] == elem && enems[j][1] == output[i])
          return 1;
      }
    }
    return 0;
  }

  int main(){

    int j = 0, i;
    cin >>T;
    char output[100];
    char invoked;
    int k;
    char temp;

    while (T-->0){
      j++;
      k = 0;
      cin >> C;
      for (i = 0; i<C; i++){
        cin >> frnds[i][0];
        cin >> frnds[i][1];
        cin >> frnds[i][2];
      }
      cin >> D;
      for (i = 0; i<D; i++){
        cin >> enems[i][0];
        cin >> enems[i][1];
      }
      cin >> N;
      for (i = 0; i<N; i++){
        cin >> invoked;
        if(k==0)
          output[k++] = invoked;
        else if (temp=pair(output[k-1], invoked))
          output[k-1] = temp;
        else if (opposed(output, k, invoked))
          k=0;
        else output[k++] = invoked;
      }

      cout << "Case #" << j << ": [";
      for (i = 0; i<k; i++){
        if(i!=0) cout << ", ";
        cout << output[i];
      }
      cout << "]" << endl;  
    }
    return 1;
  }

