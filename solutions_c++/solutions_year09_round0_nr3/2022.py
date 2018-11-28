#include <iostream>
#include <cstring>
#include <sstream>
#include <iomanip>

using namespace std;

int main()
{
  int N;
  string line;
  string::iterator it,it1,it2,it3,it4,it5,it6,it7,it8,it9,it10;
  string::iterator it11,it12,it13,it14,it15,it16,it17,it18;
  stringstream s;
  
  cin >> N;  // get number of cases
  // leftover endl
  getline(cin,line);
  
  // loop through all cases
  for (int i = 0; i < N; i++) {

    long long count = 0;           // keep track of how many times phrase appears
    getline(cin,line);       // read line
	
    // loop through each line looking for letters
	for (it = line.begin(); it < line.end(); it++) {
	  if (*it == 'w') {
	    for (it1 = it; it1 < line.end(); it1 ++) {
		  if (*it1 == 'e') {
	        for (it2 = it1; it2 < line.end(); it2 ++) {
		  if (*it2 == 'l') {
	        for (it3 = it2; it3 < line.end(); it3 ++) {
		  if (*it3 == 'c') {
	        for (it4 = it3; it4 < line.end(); it4 ++) {
		  if (*it4 == 'o') {
	        for (it5 = it4; it5 < line.end(); it5 ++) {
		  if (*it5 == 'm') {
	        for (it6 = it5; it6 < line.end(); it6 ++) {
		  if (*it6 == 'e') {
	        for (it7 = it6; it7 < line.end(); it7 ++) {
		  if (*it7 == ' ') {
	        for (it8 = it7; it8 < line.end(); it8 ++) {
		  if (*it8 == 't') {
	        for (it9 = it8; it9 < line.end(); it9 ++) {
		  if (*it9 == 'o') {
	        for (it10 = it9; it10 < line.end(); it10 ++) {
		  if (*it10 == ' ') {
	        for (it11 = it10; it11 < line.end(); it11 ++) {
		  if (*it11 == 'c') {
	        for (it12 = it11; it12 < line.end(); it12 ++) {
		  if (*it12 == 'o') {
	        for (it13 = it12; it13 < line.end(); it13 ++) {
		  if (*it13 == 'd') {
	        for (it14 = it13; it14 < line.end(); it14 ++) {
		  if (*it14 == 'e') {
	        for (it15 = it14; it15 < line.end(); it15 ++) {
		  if (*it15 == ' ') {
	        for (it16 = it15; it16 < line.end(); it16 ++) {
		  if (*it16 == 'j') {
	        for (it17 = it16; it17 < line.end(); it17 ++) {
		  if (*it17 == 'a') {
	        for (it18 = it17; it18 < line.end(); it18 ++) {
		  if (*it18 == 'm')
		    count++;
    }}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}

	count = count % 10000;
	cout << "Case #" << i+1 << ": " << setfill('0') << setw(4) << count << endl;
	
/*	stringstream ss;
	ss << count;
	string ans;
	ss >> ans;
	ans.resize(4,0);
*/
  }
  return 0;
 
}
