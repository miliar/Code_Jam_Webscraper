#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <sstream>
#include <cmath>
#include <cassert>

using namespace std;

double PI = 4.0*atan(1.0);

// We use the symmetry to only deal with a quarter of the circle.
// Instead of dealing with a fly with radius of f, we "inflate" all the 
// elements of the racquet and deal with a fly that is represented by a point.


double calculate_square_circle_area(double x_pos, double y_pos, 
				    double sq_len, double circ_rad)
{
  // find intersection with the circle.
  // from: http://mathworld.wolfram.com/Circle-LineIntersection.html

  double inter_x = sqrt(circ_rad*circ_rad - y_pos*y_pos);
  double inter_y = sqrt(circ_rad*circ_rad - x_pos*x_pos);

  assert (inter_x > x_pos);
  assert (inter_y > y_pos);

  if ((inter_x < x_pos + sq_len &&
       inter_y < y_pos + sq_len) || sq_len < 0)
    {
      // the whole section is in the square.
      double alpha = atan2(inter_y, x_pos) - atan2(y_pos, inter_x);
      // triangle area from: http://mathworld.wolfram.com/TriangleArea.html
      double tri_area = circ_rad*circ_rad*sin(alpha) / 2;
      double section_area = PI*circ_rad*circ_rad * alpha/(2*PI);
      
      return section_area - tri_area + 
	(inter_y - y_pos)*(inter_x - x_pos)/2;
    }

  // get the whole section area and substract irrelant stuff.
  double res = calculate_square_circle_area(x_pos, y_pos, 
					    -1, circ_rad);
  
  if (inter_x > x_pos + sq_len)
    res -= calculate_square_circle_area(x_pos + sq_len, y_pos, -1, circ_rad);

  if (inter_y > y_pos + sq_len)
    res -= calculate_square_circle_area(x_pos, y_pos + sq_len, -1, circ_rad);

  return res;
}


double calculate_chances(double f, double R, double t, double r, double g)
{
  // we sum the free area in a quarter of a circle. For each square we
  // sum its area.

  double free_area_in_section = 0;
  int num_of_full_sq = 0;

  double curr_x = r + f; // first square is in r + f due to inflation.
  int x_ind = 0;
  double inner_radius = R-t-f;

  while (curr_x < inner_radius)
    {
      int y_ind = 0;
      double curr_y = r + f;
      while (curr_y < inner_radius)
	{

	  // if the square is outside the circle we continue;
	  if (curr_x*curr_x + curr_y*curr_y < inner_radius*inner_radius)
	    {
	      // if the whole sqaure is in just add (g-2*f)^2.
	      double max_x = curr_x + g - 2*f;
	      double max_y = curr_y + g - 2*f;
	      if (max_x*max_x + max_y*max_y < inner_radius*inner_radius)
		{
		  ++num_of_full_sq;
		}
	      else
		{
		  // our square intersects the circle.
		  free_area_in_section += 
		    calculate_square_circle_area(curr_x, curr_y, 
						 g - 2*f, inner_radius);
		}
	    }
	  
	  ++y_ind;
	  curr_y = (r + f) + y_ind * (g + 2*r);
	}
      
      ++x_ind;
      curr_x = (r + f) + x_ind * (g + 2*r);
    }

  free_area_in_section += num_of_full_sq * (g - 2*f)*(g - 2*f);
  return free_area_in_section / (PI * R * R / 4);
}

int main()
{
  int N;
  cin >> N;

  for (int i = 0; i < N; ++i)
    {
      double f, R, t, r, g;
      cin >> f >> R >> t >> r >> g;
      
      cout << "Case #" << i + 1 << ": " << 
	1 - calculate_chances(f, R, t, r, g) << endl;
    }

  return 0;
}
