//============================================================================
// Name        : fly_swatter.cpp
// Author      : muramasa
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================
//using boost lib
#include <vector>
#include <numeric>
#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <boost/lexical_cast.hpp>
#include <boost/format.hpp>
using namespace std;
using boost::lexical_cast;

double arc_area(double left_points[2],double right_points[2],double circle_length){
	static const double pi = 3.14159265358979;
	double a = left_points[1]/left_points[0];
	double length_rsin = abs(a*right_points[0]-right_points[1])/sqrt(a*a+1);
	//cout << "left right "<< left_points[0]<<" " << left_points[1] << ", "
	//<< right_points[0] << " " << right_points[1]<<endl;
	//cout << "length_rsin : " << length_rsin << endl;
	//cout << "circle_length : " << circle_length << endl;
	double theta_ = asin(length_rsin/circle_length);
	//cout << "theta_ : " << theta_ << endl;
	double sankaku = circle_length*length_rsin/2.0;
	//cout << "sankaku : " << sankaku << endl;
	double ans = circle_length*circle_length*pi*theta_/(2*pi);
	//cout << "ans : " << ans << endl;
	return ans-sankaku;
}

int main() {
	const double pi = 3.14159265358979;
	ifstream ifs("C-small.in");
	ofstream ofs("C-small.out", std::ios::out | std::ios::trunc);
	string buf;
	getline(ifs, buf);
	int cases = lexical_cast<int> (buf);
	cout << "cases : " << cases << endl;
	for (int j = 0; j < cases; j++) {
		double f, R, t, r, g;
		ifs >> f >> R >> t >> r >> g;
		double harf_string_width = r + f;
		double gap_width = g - 2 * f;
		double between_string_width = g + 2 * r;
		double circle_length = R - t - f;
		cout << "harf_string_width : " << harf_string_width
				<< "\t gap_width : " << gap_width
				<< "\t between_string_width : " << between_string_width
				<< "\t circle_length : " << circle_length << endl;
		//ガットが何本張れるか
		int string_num = (R - t - f - harf_string_width) / between_string_width
				+ 1;
		cout << "string num : " << string_num << endl;
		double sum_area = 0.0;
		for (int x_gat = 0; x_gat < string_num; ++x_gat) {
			for (int y_gat = 0; y_gat < string_num; ++y_gat) {
				double square_points[4][2];
				//左下座標
				square_points[0][0] = harf_string_width + between_string_width
						* x_gat;
				square_points[0][1] = harf_string_width + between_string_width
						* y_gat;
				//左上座標
				square_points[1][0] = square_points[0][0];
				square_points[1][1] = square_points[0][1] + gap_width;
				//右上座標
				square_points[2][0] = square_points[0][0] + gap_width;
				square_points[2][1] = square_points[0][1] + gap_width;
				//右下座標
				square_points[3][0] = square_points[0][0] + gap_width;
				square_points[3][1] = square_points[0][1];
				if (circle_length * circle_length < square_points[0][0]
						* square_points[0][0] + square_points[0][1]
						* square_points[0][1]) {
					//必要なし（円より外
				} else if (circle_length * circle_length > square_points[2][0]
						* square_points[2][0] + square_points[2][1]
						* square_points[2][1]) {
					//完全に円の中
					sum_area += gap_width * gap_width;
				} else {
					//途中にあるとき
					double temp_left = circle_length * circle_length
							- square_points[1][0] * square_points[1][0]
							- square_points[1][1] * square_points[1][1];
					double temp_right = circle_length * circle_length
							- square_points[3][0] * square_points[3][0]
							- square_points[3][1] * square_points[3][1];
					double temp_left_points[2];
					double temp_right_points[2];
					if (temp_left <= 0 && temp_right <= 0) {
						//左下かぶり
						temp_left_points[0] = square_points[0][0];
						temp_left_points[1] = sqrt(circle_length
								* circle_length - square_points[0][0]
								* square_points[0][0]);
						temp_right_points[0] = sqrt(circle_length
								* circle_length - square_points[0][1]
								* square_points[0][1]);
						temp_right_points[1] = square_points[0][1];
						double s_sum = (temp_left_points[1]-square_points[0][1])*(temp_right_points[0]-square_points[0][0])/2.0;
						s_sum += arc_area(temp_left_points,temp_right_points,circle_length);
						//cout << "s_sum : " << s_sum <<"/" <<gap_width * gap_width<<endl;
						//cout << "左下かぶり"<< endl;
						sum_area += s_sum;
					} else if (temp_left <= 0 && temp_right > 0) {
						//左右かぶり
						temp_left_points[0] = square_points[0][0];
						temp_left_points[1] = sqrt(circle_length
								* circle_length - square_points[0][0]
								* square_points[0][0]);
						temp_right_points[0] = square_points[2][0];
						temp_right_points[1] = sqrt(circle_length
								* circle_length - square_points[2][0]
								* square_points[2][0]);
						double s_sum = (square_points[3][0]-square_points[0][0])*(temp_right_points[1]+temp_left_points[1]-square_points[0][1]*2.0)/2.0;
						s_sum += arc_area(temp_left_points,temp_right_points,circle_length);
						//cout << "s_sum : " << s_sum <<"/" <<gap_width * gap_width<<endl;
						//cout << "左右かぶり"<< endl;
						sum_area += s_sum;
					} else if (temp_left > 0 && temp_right <= 0) {
						//上下かぶり
						temp_left_points[0] = sqrt(circle_length
								* circle_length - square_points[1][1]
								* square_points[1][1]);
						temp_left_points[1] = square_points[1][1];
						temp_right_points[0] = sqrt(circle_length
								* circle_length - square_points[0][1]
								* square_points[0][1]);
						temp_right_points[1] = square_points[0][1];

						double s_sum = (square_points[1][1]-square_points[0][1])*(temp_right_points[0]+temp_left_points[0]-square_points[1][0]*2.0)/2.0;
						s_sum += arc_area(temp_left_points,temp_right_points,circle_length);
						//cout << "s_sum : " << s_sum <<"/" <<gap_width * gap_width<<endl;
						//cout << "上下かぶり"<< endl;
						sum_area += s_sum;
					} else if (temp_left > 0 && temp_right > 0) {
						//上右かぶり
						temp_left_points[0] = sqrt(circle_length
								* circle_length - square_points[1][1]
								* square_points[1][1]);
						temp_left_points[1] = square_points[1][1];
						temp_right_points[0] = square_points[3][0];
						temp_right_points[1] = sqrt(circle_length
								* circle_length - square_points[2][0]
								* square_points[2][0]);
						double s_sum= (temp_left_points[0]-square_points[1][0])*(square_points[1][1]-square_points[0][1]);
						s_sum += (square_points[3][0]-temp_left_points[0])*(temp_left_points[1]+temp_right_points[1]-square_points[3][1]*2.0)/2.0;
						s_sum += arc_area(temp_left_points,temp_right_points,circle_length);
						//cout << "s_sum : " << s_sum <<"/" <<gap_width * gap_width<<endl;
						sum_area += s_sum;
						//cout << "上右かぶり"<< endl;
						//弧の部分
					}
				}
			}
		}
		cout << "sum_area : " << sum_area << endl;
		double parcent = ((R * R * pi)/4.0 - sum_area) / ((R * R * pi)/4.0);
		cout << "parcent : " << parcent
				<< endl;

		cout << "Case #" << j+1 << ": " << boost::format("%1.6f") % parcent
		<<endl;
		ofs << "Case #" << j+1 << ": " << boost::format("%1.6f") % parcent
		<<endl;
	}
	return 0;
}
