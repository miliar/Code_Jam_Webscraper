#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <math.h>
#include "FlySwatter.h"

std::vector<std::string> separateString(std::string text, std::string delimiter)
{
	std::vector<std::string> result;
	size_t begin=0, end=0, length;

	while(end!=text.length())
	{
		begin = text.find_first_not_of(delimiter,end);
		end = text.find_first_of(delimiter, begin);
		if(end==std::string::npos)
			end = text.length();
		length = end - begin;

		result.push_back(text.substr(begin, length));
	}
	return result;
}

int main(int argc, char** argv)
{
	std::ifstream iFile(argv[1]);
	if(!iFile.is_open())
	{
		std::cerr << "No input file " << argv[1] <<std::endl;
		return 1;
	}

	std::string tmp;
	int num_case;
	std::getline(iFile, tmp);
	num_case = atoi(tmp.c_str());

	std::ofstream oFile("result.txt");

	for(int c=0; c<num_case; c++)
	{
		std::getline(iFile, tmp);
		std::vector<std::string> case_i(5);
		case_i= separateString(tmp," ");
		long double f, R, t, r, g, R_in;
		f = atof(case_i[0].c_str());
		R = atof(case_i[1].c_str());
		t = atof(case_i[2].c_str());
		r = atof(case_i[3].c_str());
		g = atof(case_i[4].c_str());
		R_in = R-t;

		if( 2*f >= g )	// the fly is bigger than the racket's hole
		{
			oFile << "Case #" << c+1 << ": 1.000000" << std::endl;
			continue;
		}

		// Calculate event & prob. for a quarter of the racket only (symmetric)
		int num_full_hole = 0;
		long double e_full_hole = (g-2*f) * (g-2*f);
		long double e_no_hit = 0;	// event that the fly pass through racket's hole
		long double e_all = 0.25 * PI * R * R; // 1/4 of racket area
		long double r_current = -r*sqrt(2.0);
		int round = 0;

		while(r_current/sqrt(2.0) <= R_in)
		{
			if(r_current + sqrt(2.0)*(g+2*r) <= R_in) 
				// full hole
			{
				num_full_hole += 2*round + 1;
			}
			else
				// partly
			{
				int hole_to_check = round+1;
				Point bl(r+round*(g+2*r), r+round*(g+2*r));
				Point br(r+round*(g+2*r)+g, r+round*(g+2*r));
				Point tl(r+round*(g+2*r), r+round*(g+2*r)+g);
				Point tr(r+round*(g+2*r)+g, r+round*(g+2*r)+g);
				Point bl_in(bl.x+2*f, bl.y+2*f);
				//Point br_in(br.x-2*f, br.y+2*f);
				//Point tl_in(tl.x+2*f, tl.y-2*f);
				//Point tr_in(tr.x-2*f, tr.y-2*f);

				while(hole_to_check > 0)
				{
					if(isInsideCircle(bl_in, R_in))
						// inside racket area
					{
						if(isInsideCircle(tr, R_in))	// full hole
						{
							num_full_hole += hole_to_check * 2;	// symmetry
							hole_to_check = 0;
						}
						else 
						{
							long double w = tr.x-f;
							long double h = tr.y-f;
							long double R2 = R_in-f;
							long double theta, theta1, theta2;
							long double e_in, e_out;
							long double w1, h1, h2, w2;

							if(isInsideCircle(tl, R_in))
								// top left & bottom right corners are inside
							{
								w1 = sqrt(R2*R2 - h*h);
								h1 = sqrt(R2*R2 - w*w);
								theta2 = atan(h/w1);
								theta1 = atan(h1/w);
								theta = abs(theta2-theta1);
								e_out = w*h - 0.5*w*h1 - 0.5*w1*h - 0.5*theta*R2*R2;
								e_in = e_full_hole - e_out;
								
								if(bl.x==bl.y)
									e_no_hit += e_in;
								else
									e_no_hit += e_in * 2;	//symmetry
							}
							else if(isInsideCircle(br, R_in))
								// bottom right corner is inside
							{
								h1 = sqrt(R2*R2 - w*w);
								w2 = bl.x + f;
								h2 = sqrt(R2*R2 - w2*w2);
								theta2 = atan(h2/w2);
								theta1 = atan(h1/w);
								theta = theta2 - theta1;
								e_out = w*h - 0.5*w*h1 - 0.5*w2*(h+h-h2) - 0.5*theta*R2*R2;
								e_in = e_full_hole - e_out;
								e_no_hit += e_in * 2;	// symmetry
							}
							else
								// only bottom left corner is inside -- tested
							{
								h1 = bl.y + f;
								w1 = sqrt(R2*R2 - h1*h1);
								w2 = bl.x + f;
								h2 = sqrt(R2*R2 - w2*w2);
								theta2 = atan(h2/w2);
								theta1 = atan(h1/w1);
								theta = abs(theta2-theta1);
								e_out = w*h - 0.5*w2*(h+h-h2) - 0.5*h1*(w+w-w1) - 0.5*theta*R2*R2;

								e_in = e_full_hole - e_out;
								if(bl.x==bl.y)
									e_no_hit += e_in;
								else
									e_no_hit += e_in * 2;	//symmetry
							}
						}
					}
					hole_to_check--;
					movePoint(bl, -(g+2*r), 0);
					movePoint(br, -(g+2*r), 0);
					movePoint(tl, -(g+2*r), 0);
					movePoint(tr, -(g+2*r), 0);
					movePoint(bl_in, -(g+2*r), 0);
					//movePoint(br_in, -(g+2*r), 0);
					//movePoint(tl_in, -(g+2*r), 0);
					//movePoint(tr_in, -(g+2*r), 0);	

				}
			}
			++round;
			r_current += sqrt(2.0)*(g+2*r);
		}

		e_no_hit += num_full_hole * e_full_hole;
		long double p_hit = 1.0 - (e_no_hit / e_all);
		oFile.precision(0);
		oFile << "Case #" << c+1 << ": ";
		oFile.precision(6);
		oFile << std::fixed << p_hit << std::endl;
	}
	oFile.close();
	iFile.close();
	return 0;
}

void movePoint(Point &p, long double dx, long double dy)
{
	p.x += dx;
	p.y += dy;
}

bool isInsideCircle(const Point &p, const long double &radius)
{
	if(sqrt(p.x*p.x + p.y*p.y) < radius)
		return true;
	else 
		return false;
}
