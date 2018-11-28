//---------------------------------------------------------------------------

#include <stdio.h>
#include <math.h>

//---------------------------------------------------------------------------

double integ(double f, double R, double t, double r, double g)
{
  double x, y, dx;
  double PI = 3.1415926535897932384626433832795; //3.1415926535898;
  double prec = 2000000 * PI;
  dx = R / prec;

  double R_, t_, r_, g_, R2, R_2;
  t_ = t + f;
  r_ = r + f;
  g_ = g - 2 * f;
  R_ = R - t_;

  R2 = R * R;
  R_2 = R_ * R_;

  double all_area, in_area, out_area;
  all_area = PI * R2;
  in_area = PI * R_2;
  out_area = all_area - in_area;

  x = dx / 2;

  double next_r_bound, next_l_bound;
  next_r_bound = r_;
  next_l_bound = r_ + g_;

  double total_len = 0, hit_len = 0;

  while (x < R_)
  {

	while ((x < next_r_bound) && (x < R_))
	{
	  y = sqrt(R_2 - x * x);
	  total_len += y;
	  hit_len += y;
	  x += dx;
	}

	while ((x < next_l_bound) && (x < R_))
	{
	  y = sqrt(R_2 - x * x);
	  total_len += y;
	  int horiz_str_count;
	  if (y > r_)
		  horiz_str_count = (y - r_) / (g_ + 2 * r_);
	  else horiz_str_count = 0;
	  double total_str_height = (horiz_str_count * 2 + (y > r_)) * r_;
	  double total_gap_height = (horiz_str_count) * g_;
	  double total_int_height = total_str_height + total_gap_height;
	  double next_b_bound = total_int_height + g_;
	  if (next_b_bound < y)
		total_str_height += (y - next_b_bound);
//		total_str_height += (y - next_b_bound - 2 * r_);
	  hit_len += total_str_height;
//	  hit_len += y;
	  x += dx;
	}

	next_r_bound += g_ + (2 * r_);
	next_l_bound += g_ + (2 * r_);
  }

  return (((hit_len / total_len) * in_area) + out_area) / all_area;
}

//---------------------------------------------------------------------------

int main()
{
  int N;
  double f, R, t, r, g;
  double prob;
  FILE * inFile, * outFile;
  inFile = fopen ("C:\\Documents and Settings\\Risky\\My Documents\\Borland Studio Projects\\fly_swatter\\C-large.in","r");
  outFile = fopen ("C:\\Documents and Settings\\Risky\\My Documents\\Borland Studio Projects\\fly_swatter\\C-large.out","w");
  if (inFile!=NULL)
  {
	fscanf (inFile, "%d", &N);
	for (int i = 1; i <= N; i++)
	{
		fscanf (inFile, "%lf", &f);
		fscanf (inFile, "%lf", &R);
		fscanf (inFile, "%lf", &t);
		fscanf (inFile, "%lf", &r);
		fscanf (inFile, "%lf", &g);

		prob = integ(f, R, t, r ,g);

		fprintf (outFile, "Case #%d: %lf\n", i, prob);
	}

	fclose (inFile);
	fclose (outFile);

  }

  return 0;
}
//---------------------------------------------------------------------------
