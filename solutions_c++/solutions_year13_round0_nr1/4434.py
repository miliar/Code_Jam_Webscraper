#include <stdio.h>

void reset_count(int *count, bool flag = false)
{
  
  for(int j = 0; j < 3; j++)
    count[j] = 0;

  if(flag)
    count[3] = 0; 
}

int set_status(int *count)
{
  int status;

  for(int i = 0; i < 4; i++)
  //printf("count[%d] = %d\t", i, count[i]);

  //printf("\n");


  if(count[0] + count[2] == 4)
    status = 1;
  else if(count[1] + count[2] == 4)
    status = 2;
  else
    status = 3;

  reset_count(count);

    return status;
}

int main()
{
  int T;
  char matrix[4][5];

  int count[4] = {0};
  int status = 0;
   
  
  scanf("%d", &T);
  for(int tc = 1; tc <= T; tc++)
  {
    for(int i = 0; i < 4; i++)
    {
        scanf("%s", matrix[i]);
       // printf("%s\n", matrix[i]);
    }
    //printf("\n");
    
    status  =0;
    reset_count(count, true);
    
    //Row Wise
    //printf("Row Wise\n");
    for(int i = 0; i < 4; i++)
    {
      
      if(status == 1 || status == 2)
        break;
      
      for(int j = 0; j < 4; j++)
      {
        if(matrix[i][j] == 'X')
          count[0]++;
        else if(matrix[i][j] == 'O')  
          count[1]++;
        else if(matrix[i][j] == 'T')
          count[2] = 1;
        else
          count[3]++;
      }
      
      status = set_status(count);
    }

    //printf("status = %d\n", status);

    //printf("Column Wise\n");
    for(int i = 0; i < 4; i++)
    {
      
      if(status == 1 || status == 2)
        break;
      
      for(int j = 0; j < 4; j++)
      {
        if(matrix[j][i] == 'X')
          count[0]++;
        else if(matrix[j][i] == 'O')  
          count[1]++;
        else if(matrix[j][i] == 'T')
          count[2] = 1;
        else
          count[3]++;
      }
      
      status = set_status(count);
    }

    //printf("status = %d\n", status);


    //printf("Diagonal wise\n");
    for(int i = 0; i < 4; i++)
    {
      if(status == 1 || status == 2)
        break;

      if(matrix[i][i] == 'X')
          count[0]++;
        else if(matrix[i][i] == 'O')  
          count[1]++;
        else if(matrix[i][i] == 'T')
          count[2] = 1;
        else
          count[3]++;
    }
    
    if(status == 3)
    status = set_status(count);

   // printf("status = %d\n", status);


    //printf("Cross-Diagonal Wise\n");
    for(int i = 0; i < 4; i++)
    {
      if(status == 1 || status == 2)
        break;

      if(matrix[i][3-i] == 'X')
          count[0]++;
        else if(matrix[i][3-i] == 'O')  
          count[1]++;
        else if(matrix[i][3-i] == 'T')
          count[2] = 1;
        else
          count[3]++;
    }
    
    if(status == 3)
      status = set_status(count);

    //printf("status = %d\n", status);


    if(status == 1)
      printf("Case #%d: X won\n", tc);
    else if (status == 2)
      printf("Case #%d: O won\n", tc);
    else
    {
      if(count[3] == 0)
        printf("Case #%d: Draw\n", tc);
      else
        printf("Case #%d: Game has not completed\n", tc);

    }
  }
}

