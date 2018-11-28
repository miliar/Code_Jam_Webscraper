#include <stdio.h>
#include <string.h>
#include <math.h>

#define M_PI       3.14159265358979323846
#define M_PI_2     1.57079632679489661923
#define M_PI_4     0.785398163397448309616

int N;
long double f, R, t, r, g;


long double GetSquare(long double X, long double Y, long double Size){
  long double Sum = 0.0;
  long double ShiftX = 0.0, ShiftY = 0.0;
  long double CrossX, CrossY;
  long double A, B, C, alpha;

  if( X >= Y ){
    if( ( X*X + (Y+Size)*(Y+Size) ) < (R-t-f)*(R-t-f) ){
      ShiftX = sqrt((R-t-f)*(R-t-f) - (Y+Size)*(Y+Size) ) - X;
      Sum += Size*ShiftX;
      if( ( (X+Size)*(X+Size) + Y*Y ) < (R-t-f)*(R-t-f) ){
        Sum -= GetSquare(X+Size,Y,Size);
      }
      X = X + ShiftX;
    }
    
/*    if( ( (X+Size)*(X+Size) + Y*Y ) < (R-t-f)*(R-t-f) ){
      ShiftY = sqrt((R-t-f)*(R-t-f) - (X+Size)*(X+Size) ) - Y;
      Sum += (Size-ShiftX)*ShiftY;
      Y = Y + ShiftY;
    }
*/  }
  else{
    if( ( (X+Size)*(X+Size) + Y*Y ) < (R-t-f)*(R-t-f) ){
      ShiftY = sqrt((R-t-f)*(R-t-f) - (X+Size)*(X+Size) ) - Y;
      Sum += Size*ShiftY;
      if( ( X*X + (Y+Size)*(Y+Size) ) < (R-t-f)*(R-t-f) ){
        Sum -= GetSquare(X,Y+Size,Size);
      }
      Y = Y + ShiftY;
    }
/*    if( ( X*X + (Y+Size)*(Y+Size) ) < (R-t-f)*(R-t-f) ){
      ShiftX = sqrt((R-t-f)*(R-t-f) - (Y+Size)*(Y+Size) ) - X;
      Sum += (Size-ShiftY)*ShiftX;
      X = X + ShiftX;
    }
*/  }

  if( ( X*X + Y*Y ) >= (R-t-f)*(R-t-f) ){
    return Sum;
  }
  
  CrossX = sqrt((R-t-f)*(R-t-f) - Y*Y );
  CrossY = sqrt((R-t-f)*(R-t-f) - X*X );
  A = CrossX - X;
  B = CrossY - Y;
  Sum += 0.5 * A * B;
  C = sqrt( A*A + B*B );
  alpha = asin(C/(2*((R-t-f))));
  Sum += alpha * (R-t-f) * (R-t-f);
//  Sum -= 0.5 * (R-t-f) * cos(alpha)* C;
  Sum -= 0.5 * (R-t-f) * (R-t-f) * sin(2*alpha);

  return Sum;
}

long double Solver(void){
  long double Sum, Prob;
  long double CurrentX, CurrentY, CurrentXMax1, CurrentXMax2, CurrentYMax;
  long double SquareSize;
  long double alpha;
  long Squares;

  if( g <= 2*f ){
    return 1.0;
  }
  if( R - t - f <= 0.0 ){
    return 1.0;
  }

  Sum = 0.0;
  Squares = 0;
  SquareSize = g - 2 * f;
  alpha = asin( (r+f)/(R-t-f) );
  CurrentYMax = (R-t-f) * cos(alpha);
//  CurrentYMax = sqrt( (R-t-f)*(R-t-f) - (r+f)*(r+f) );
  for( CurrentY = r+f; CurrentY < CurrentYMax; CurrentY += g + 2 * r ){
    alpha = asin( CurrentY / (R-t-f) );
    CurrentXMax1 = cos(alpha) * (R-t-f);
    alpha = asin( (CurrentY+SquareSize) / (R-t-f) );
    CurrentXMax2 = cos(alpha) * (R-t-f);
//    CurrentXMax1 = sqrt( (R-t-f)*(R-t-f) - CurrentY*CurrentY );
//    CurrentXMax2 = sqrt( (R-t-f)*(R-t-f) - (CurrentY+SquareSize)*(CurrentY+SquareSize) );
    for( CurrentX = r+f; CurrentX < CurrentXMax1; CurrentX += g + 2 * r ){
      if( CurrentX + SquareSize <= CurrentXMax2 ){
        Squares ++;
      }
      else{
        Sum += GetSquare(CurrentX, CurrentY, SquareSize);
      }
    }
  }

  Prob = 1 - 4 * ( Squares*SquareSize*SquareSize + Sum ) / ( M_PI * R * R );
  return (float)Prob;
}

int main(int argc, char *argv[]){
  FILE* file;
  FILE* fileout;
  int n, i;
  float res;

  if( argc < 2 ){
    printf("Usage is: task1 filename\n");
    return 0;
  }

  /* Input */

  file = fopen(argv[1], "r");
  if( file == NULL ){
    printf("Error open();\n");
    return 0;
  }
  fileout = fopen("res.txt", "w");


  fscanf(file, "%d\n", &N);
  for( n = 0; n < N; n ++ ){
    fscanf(file, "%lf %lf %lf %lf %lf\n", &f, &R, &t, &r, &g);
    printf("%d -------------\n", N);
    printf("%lf %lf %lf %lf %lf\n", f, R, t, r, g);

    /* Solving */
    res = Solver();
    /* Output */
    fprintf(fileout, "Case #%d: %.6f\n", n+1, res);
  }

  fclose(fileout);
  fclose(file);

  return 0;
}
