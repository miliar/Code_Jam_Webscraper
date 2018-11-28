#include <iostream>
#include <iomanip>
#include <fstream>
#include <cmath>

std::ifstream in("fly.in");
std::ofstream out("fly.out");

double calc_1(double x)
{
    return .5 * (sqrt(1-x*x)*x + asin(x)); 
}

double calc_2(double left, double right)
{
    return calc_1(right) - calc_1(left);
}

double calc_area(double left, double right, double bottom, double top)
{

    double ltop = sqrt(1 - left*left);
    double rtop = sqrt(1 - right*right);
    double bright = sqrt(1 - bottom*bottom);
    double tright = sqrt(1 - top*top);

    double area = -1;

    if (left * left + bottom * bottom > 1)
        return 0;

    if (top * top + right * right > 1) {
        if (top < ltop && right < bright) {
            area = (sqrt(1 - top * top) - left) * (top - bottom);
            area += calc_2(sqrt(1 - top * top), right);
            area -= (right - sqrt(1 - top * top)) * bottom;
        } else if (top >= ltop && right < bright) {
            area = calc_2(left, right);
            area -= bottom * (right - left);
        } else if (top < ltop && right >= bright) {
            area = calc_area(bottom, top, left, right);
        } else {
            area = calc_2(left, bright);
            area -= bottom * (bright - left);
        }
    } else
        area = (right - left) * (top - bottom);

    return area;
}

double calc(double radius, double left, double right, double bottom, double top)
{
    return radius * radius * calc_area(left/radius, right/radius, bottom/radius, top/radius);
}

int cases;

double process()
{
    double f, R, t, r, g;
    in >> f >> R >> t >> r >> g;

    r += f;
    g -= 2 * f;
    if (g < 0)
        return 1;

    t += f;
    if (t >= R)
        return 1;

    double area = 0;
    area += calc(R-t, 0, r, 0, R);

    for (double left = r + g; left < R - t; left += g + 2 * r)
        area += calc(R-t, left, left + 2 * r, 0, R);

    area *= 2;
    area -= calc(R-t, 0, r, 0, r);

    for (double left = r + g; left < R - t; left += g + 2 * r)
    for (double bottom = r + g; bottom < R - t; bottom += g + 2 * r)
        area -= calc(R-t, left, left + 2 * r, bottom, bottom + 2 * r);

    double waste = 0;
    for (double left = r + g; left < R - t; left += g + 2 * r)
        waste += calc(R-t, left, left + 2 * r, 0, r);

    area -= waste * 2;

    return (area + calc(R, 0, R, 0, R) - calc(R-t, 0, R, 0, R)) / calc(R, 0, R, 0, R);
}

int main()
{
    in >> cases;

    for (int i = 0; i < cases; i++)
        out << "Case #" << i + 1 << ": " << std::fixed << std::setprecision(6) << process() << "\n"; 
    return 0;
}

