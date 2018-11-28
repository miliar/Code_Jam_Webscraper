#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <ctime>
#include <limits>
using namespace std;

#pragma warning(disable: 4018)


//template <typename KT, typename T> bool has_key(map<KT, T> &map, KT &key)
//{
//	return map.find(key) != map.end;
//}
//
//template <typename KT, typename T> bool get_value_or_default(map<KT, T> &map, KT &key, T &default_value)
//{
//	if (map.find(key) != map.end)
//		return map[key];
//	else
//		return default_value;
//}

//template <typename T1, typename T2, typename T3> void repeated_read_print(int n, ifstream &ifs, 
//		vector<T1> &v1, vector<T2> &v2, vector<T3> &v3)
//{
//	for (int i=0 ; i < n ; i++)
//	{
//		T1 x1;
//		T2 x2;
//		T3 x3;
//
//		ifx >> x1 >> x2 >> x3;
//
//		cout << x1 << " " << x2 << " " << x3 << " " << endl;
//
//		v1.push_back(x1);
//		v2.push_back(x2);
//		v3.push_back(x3);
//	}
//}


//template <typename T> string to_string(vector<T> &v)
//{
//	string res = "";
//	for (int i=0 ; i < v.size() ; i++)
//	{
//		if (i > 0)
//			res += " ";
//		res += (string) v[i];
//	}
//	return res;
//}

//#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
//#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
//#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
//#define Repd(i,n) for (int i((n)-1); i >= 0; --i)

#define repeat(i, n) for (int i(0), _n(n) ; i < _n ; i++)
#define loop(i, m, n) for (int i((m)), _n(n) ; i < _n ; i++)


typedef long long intw;

typedef vector<bool> bool_v;
typedef vector<int> int_v;
typedef vector<double> double_v;
typedef vector<char> char_v;
typedef vector<string> str_v;
typedef vector<intw> intw_v;

/*************************************************************************************/

vector<string> split(const string &str, char separator)
{
	vector<string> res;

	int len = str.length();

	int offset = 0;

	for ( ; ; )
	{
		int leading_sep_count = 0;
		for (int i=0 ; offset + i < len && str[offset + i] == separator ; i++)
			leading_sep_count++;

		if (offset + leading_sep_count == len)
			break;

		offset += leading_sep_count;

		int fragment_length = 0;
		for (int i=0 ; offset + i < len && str[offset + i] != separator ; i++)
			fragment_length++;

		string fragment = str.substr(offset, fragment_length);

		res.push_back(fragment);

		offset += fragment_length;
	}

	return res;
}

int to_int(const string &str)
{
	stringstream ss(str);

	int res;
	ss >> res;

	assert(!ss.fail());

	return res;
	//return atoi(str.c_str());
}

long long to_intw(const string &str)
{
	stringstream ss(str);

	long long res;
	ss >> res;

	assert(!ss.fail());

	return res;
	//return atoi(str.c_str());
}

double to_double(const string &str)
{
	stringstream ss(str);

	double res;
	ss >> res;

	assert(!ss.fail());

	return res;
}

vector<int> to_ints(const string &str, char separator = ' ')
{
	vector<string> int_strs = split(str, separator);

	vector<int> ints(int_strs.size());
	for (int i=0 ; i < int_strs.size() ; i++)
		ints[i] = to_int(int_strs[i]);

	return ints;
}

vector<intw> to_intws(const string &str, char separator = ' ')
{
	vector<string> intw_strs = split(str, separator);

	vector<intw> intws(intw_strs.size());
	for (int i=0 ; i < intw_strs.size() ; i++)
		intws[i] = to_intw(intw_strs[i]);

	return intws;
}

vector<double> to_doubles(const string &str, char separator = ' ')
{
	vector<string> double_strs = split(str, separator);

	vector<double> doubles(double_strs.size());
	for (int i=0 ; i < double_strs.size() ; i++)
		doubles[i] = to_double(double_strs[i]);

	return doubles;
}

string get_line(ifstream &ifs)
{
	string res;
	getline(ifs, res);
	return res;
}

/*************************************************************************************/

template <typename T> string to_string(vector<T> &v)
{
	ostringstream os;

	for (int i=0 ; i < v.size() ; i++)
	{
		if (i > 0)
			os << " ";
		os << v[i];
	}

	return os.str();
}

/*************************************************************************************/

int get_int(ifstream &ifs, const string &label = "")
{
	int n = to_int(get_line(ifs));

	if (label.length() > 0)
		cout << label << ": ";
	cout << n << endl;

	return n;
}

intw get_intw(ifstream &ifs, const string &label = "")
{
	intw n = to_intw(get_line(ifs));

	if (label.length() > 0)
		cout << label << ": ";
	cout << n << endl;

	return n;
}

double get_double(ifstream &ifs, const string &label = "")
{
	double x = to_double(get_line(ifs));

	if (label.length() > 0)
		cout << label << ": ";
	cout << x << endl;

	return x;
}

vector<int> get_ints(ifstream &ifs, const string &label = "", char separator = ' ')
{
	vector<int> ns = to_ints(get_line(ifs), separator);

	if (label.length() > 0)
		cout << label << ": ";
	cout << to_string(ns) << endl;

	return ns;
}

vector<intw> get_intws(ifstream &ifs, const string &label = "", char separator = ' ')
{
	vector<intw> ns = to_intws(get_line(ifs), separator);

	if (label.length() > 0)
		cout << label << ": ";
	cout << to_string(ns) << endl;

	return ns;
}

vector<double> get_doubles(ifstream &ifs, const string &label = "", char separator = ' ')
{
	vector<double> xs = to_doubles(get_line(ifs), separator);

	if (label.length() > 0)
		cout << label << ": ";
	cout << to_string(xs) << endl;

	return xs;
}

vector<string> get_strs(ifstream &ifs, const string &label = "", char separator = ' ', bool silently = false)
{
	vector<string> strs = split(get_line(ifs), separator);

	if (!silently)
	{
		if (label.length() > 0)
			cout << label << ": ";

		for (int i=0 ; i < strs.size() ; i++)
			cout << (i > 0 ? " - " : "") << '"' << strs[i] << '"';
		cout << endl;
	}

	return strs;
}

template <typename T> void dump(T &obj, const string &label = "")
{
	if (label.length() > 0)
		cout << label << ": ";
	cout << to_string(obj) << endl;
}

template <typename T> vector<int> get_indexes(const vector<T> &subset, const vector<T> &superset)
{
	int n = subset.size();
	int m = superset.size();

	vector<int> indexes(n);

	for (int i=0 ; i < n ; i++)
	{
		indexes[i] = -1;

		for (int j=0 ; j < m ; j++)
			if (subset[i] == superset[j])
			{
				indexes[i] = j;
				break;
			}

		assert(indexes[i] != -1);
	}

	assert(take_by_index(indexes, superset) == subset);

	return indexes;
}

template <typename T>  int get_index_into_sorted_set(T element, const vector<T> &v)
{
	int n = v.size();

	int low = 0;
	int high = n - 1;

	while (low < high)
	{
		int mid = (low + high) / 2;
		
		if (v[mid] == element)
			return mid;

		if (v[mid] > element)
			high = mid - 1;
		else
			low = mid + 1;
	}

	//	Not found!
	assert(false);

	return -1;
}

template <typename T> vector<int> get_indexes_into_sorted_set(const vector<T> &subset, const vector<T> &superset)
{
	int n = subset.size();
	int m = superset.size();

	vector<int> indexes(n);

	for (int i=0 ; i < n ; i++)
		indexes[i] = get_index_into_sorted_set(subset[i], superset);

	return indexes;
}

template <typename T> vector<T> take_by_index(const vector<int> &indexes, const vector<T> &elements)
{
	int n = indexes.size();

	vector<T> res(n);

	for (int i=0 ; i < n ; i++)
		res[i] = elements[indexes[i]];

	return res;
}

template <typename T> bool is_sorted(vector<T> v, bool asc)
{
	for (int i=0 ; i < v.size() - 1 ; i++)
		if ((asc && v[i] > v[i+1]) || (!asc	&& v[i] < v[i+1]))
			return false;

	return true;
}

template <typename T> vector<int> sorted_indexes(vector<T> &elements, bool asc=true)
{
	vector<int> indexes = inc_vector(0, elements.size());
	sort_values_only_by_key(indexes, elements, asc);

	assert(is_sorted(take_by_index(indexes, elements), asc));

	return indexes;
}

template <typename ET, typename KT> void sort_values_only_by_key(vector<ET> &elements, vector<KT> keys, bool asc=true)
{
	sort_by_key(elements, keys, asc);
}

template <typename T> void sort(vector<T> &v, bool asc=true)
{
	sort(v.begin(), v.end());
	if (!asc)
		reverse(v.begin(), v.end());
}

template <typename ET, typename KT> void sort_by_key(vector<ET> &elements, vector<KT> &keys, bool asc=true)
{
	assert(elements.size() == keys.size());

	int n = elements.size();

	for (int i=0 ; i < n-1 ; i++)
		for (int j=i+1 ; j < n ; j++)
			if ((asc && keys[i] > keys[j]) || (!asc && keys[i] < keys[j]))
			{
				swap(elements[i], elements[j]);
				swap(keys[i], keys[j]);
			}

	//assert(is_sorted(elements, asc));
	assert(is_sorted(keys, asc));
}

template <typename T> T rep_add(const vector<T> &items, const T &value_if_emtpy)
{
	int n = items.size();

	if (n == 0)
		return value_if_emtpy;

	if (n == 1)
		return items[0];

	T res = items[0] + items[1];

	for (int i=2 ; i < n ; i++)
		res = res + items[i];

	return res;
}

template <typename T> vector<T> inc_vector(T first, int count)
{
	vector<T> v(count);

	for (int i=0 ; i < count ; i++)
		v[i] = first + i;

	return v;
}

template <typename T> vector<T> rep_vector(const T &value, int count)
{
	vector<T> res(count);

	for (int i=0 ; i < count ; i++)
		res[i] = value;

	return res;
}

template <typename T> vector<T> concatenate(vector<T> &v1, vector<T> &v2)
{
	int n1 = v1.size();
	int n2 = v2.size();

	vector<T> res(n1+n2);

	for (int i=0 ; i < n1 ; i++)
		res[i] = v1[i];

	for (int i=0 ; i < n2 ; i++)
		res[i+n1] = v2[i];

	return res;
}

template <typename T> vector<T> subvector(const vector<T> &v, int first, int count)
{
	vector<T> res(count);

	for (int i=0 ; i < count ; i++)
		res[i] = v[i + first];

	return res;
}

template <typename T> vector<T> left_subvector(const vector<T> &v, int size)
{
	vector<T> res(size);

	for (int i=0 ; i < size ; i++)
		res[i] = v[i];

	return res;
}

template <typename T> vector<T> right_subvector(const vector<T> &v, int size)
{
	vector<T> res(size);

	int n = v.size();

	for (int i=0 ; i < size ; i++)
		res[i] = v[n - size + i];

	return res;
}

string to_string_from_char_v(const vector<char> &v)
{
	int n = v.size();

	string str(n, ' ');

	for (int i=0 ; i < n ; i++)
		str[i] = v[i];

	return str;
}

vector<char> to_char_v(const string &str)
{
	int n = str.length();

	vector<char> v(n);

	for (int i=0 ; i < n ; i++)
		v[i] = str[i];

	assert(to_string_from_char_v(v) == str);

	return v;
}

template <typename T> vector<T> sort_and_remove_duplicates(vector<T> v)
{
	vector<T> res;

	sort(v);

	//	TODO: try to rewrite it with a do while loop
	T curr_el;
	for (int i=0 ; i < v.size() ; i++)
		if (i == 0 || v[i] != curr_el)
		{
			curr_el = v[i];
			res.push_back(curr_el);
		}

	for (int i=0 ; i < res.size()-1 ; i++)
		assert(res[i] < res[i+1]);

	return res;
}

template <typename T> vector<T> intermix(const vector<T> &vs, const T &v)
{
	int n = vs.size();

	vector<T> res(2*n - 1);

	for (int i=0 ; i < n ; i++)
		res[2*i] = vs[i];

	for (int i=0 ; i < n-1 ; i++)
		res[2*i + 1] = v;

	return res;
}

string to_string(int n)
{
	stringstream ss;
	ss << n;
	return ss.str();
}

string to_string(double x)
{
	stringstream ss;
	ss << x;
	return ss.str();
}

void to_any(const string &str, int &val)
{
	val = to_int(str);
}

void to_any(const string &str, intw &val)
{
	val = to_intw(str);
}

void to_any(const string &str, double &val)
{
	val = to_double(str);
}

void to_any(const string &str, string &val)
{
	val = str;
}

string to_string(string str)
{
	return '"' + str + '"';
}

string to_string(long long n)
{
	stringstream ss;
	ss << n;
	return ss.str();
}

template <typename T> void logged_to_any(const string &str, T &val, const string &label)
{
	to_any(str, val);
	if (label.length() > 0)
		cout << label << ": ";
	cout << to_string(val) << endl;
}

template <typename T> void get_anys(ifstream &ifs, T &val, const string &label = "", char separator = ' ')
{
	vector<string> strs = get_strs(ifs, "", separator);

	logged_to_any(strs[0], val, label);
}

template <typename T1, typename T2> void get_anys(ifstream &ifs, T1 &val1, T2 &val2, string label1, string label2, char separator = ' ')
{
	vector<string> strs = get_strs(ifs, "", separator);

	logged_to_any(strs[0], val1, label1);
	logged_to_any(strs[1], val2, label2);
}

template <typename T1, typename T2, typename T3> void get_anys(ifstream &ifs, T1 &val1, T2 &val2, T3 &val3, string label1, string label2, string label3, char separator = ' ')
{
	vector<string> strs = get_strs(ifs, "", separator, true);

	logged_to_any(strs[0], val1, label1);
	logged_to_any(strs[1], val2, label2);
	logged_to_any(strs[2], val3, label3);
}

template <typename T1, typename T2, typename T3, typename T4>
void get_anys(ifstream &ifs, T1 &val1, T2 &val2, T3 &val3, T4 &val4,
							string label1, string label2, string label3, string label4, char separator = ' ')
{
	vector<string> strs = get_strs(ifs, "", separator, true);

	logged_to_any(strs[0], val1, label1);
	logged_to_any(strs[1], val2, label2);
	logged_to_any(strs[2], val3, label3);
	logged_to_any(strs[3], val4, label4);
}

template <typename T1, typename T2, typename T3, typename T4, typename T5>
void get_anys(ifstream &ifs, T1 &val1, T2 &val2, T3 &val3, T4 &val4, T5 &val5,
							string label1, string label2, string label3, string label4, string label5, char separator = ' ')
{
	vector<string> strs = get_strs(ifs, "", separator, true);

	logged_to_any(strs[0], val1, label1);
	logged_to_any(strs[1], val2, label2);
	logged_to_any(strs[2], val3, label3);
	logged_to_any(strs[3], val4, label4);
	logged_to_any(strs[4], val5, label5);
}

template <typename T1, typename T2, typename T3, typename T4, typename T5, typename T6>
void get_anys(ifstream &ifs, T1 &val1, T2 &val2, T3 &val3, T4 &val4, T5 &val5, T6 &val6,
							string label1, string label2, string label3, string label4, string label5, string label6, char separator = ' ')
{
	vector<string> strs = get_strs(ifs, "", separator, true);

	logged_to_any(strs[0], val1, label1);
	logged_to_any(strs[1], val2, label2);
	logged_to_any(strs[2], val3, label3);
	logged_to_any(strs[3], val4, label4);
	logged_to_any(strs[4], val5, label5);
	logged_to_any(strs[5], val6, label6);
}

template <typename T1, typename T2, typename T3, typename T4, typename T5, typename T6, typename T7>
void get_anys(ifstream &ifs, T1 &val1, T2 &val2, T3 &val3, T4 &val4, T5 &val5, T6 &val6, T7 &val7,
							string label1, string label2, string label3, string label4, string label5, string label6, string label7, char separator = ' ')
{
	vector<string> strs = get_strs(ifs, "", separator, true);

	logged_to_any(strs[0], val1, label1);
	logged_to_any(strs[1], val2, label2);
	logged_to_any(strs[2], val3, label3);
	logged_to_any(strs[3], val4, label4);
	logged_to_any(strs[4], val5, label5);
	logged_to_any(strs[5], val6, label6);
	logged_to_any(strs[6], val7, label7);
}

template <typename T1, typename T2, typename T3, typename T4, typename T5, typename T6, typename T7, typename T8>
void get_anys(ifstream &ifs, T1 &val1, T2 &val2, T3 &val3, T4 &val4, T5 &val5, T6 &val6, T7 &val7, T8 &val8,
							string label1, string label2, string label3, string label4, string label5, string label6, string label7, string label8, char separator = ' ')
{
	vector<string> strs = get_strs(ifs, "", separator, true);

	logged_to_any(strs[0], val1, label1);
	logged_to_any(strs[1], val2, label2);
	logged_to_any(strs[2], val3, label3);
	logged_to_any(strs[3], val4, label4);
	logged_to_any(strs[4], val5, label5);
	logged_to_any(strs[5], val6, label6);
	logged_to_any(strs[6], val7, label7);
	logged_to_any(strs[7], val8, label8);
}

#define read1(V)															get_anys(ifs, V, #V)
#define read2(V1, V2)													get_anys(ifs, V1, V2, #V1, #V2)
#define read3(V1, V2, V3)											get_anys(ifs, V1, V2, V3, #V1, #V2, #V3)
#define read4(V1, V2, V3, V4)									get_anys(ifs, V1, V2, V3, V4, #V1, #V2, #V3, #V4)
#define read5(V1, V2, V3, V4, V5)							get_anys(ifs, V1, V2, V3, V4, V5, #V1, #V2, #V3, #V4, #V5)
#define read6(V1, V2, V3, V4, V5, V6)					get_anys(ifs, V1, V2, V3, V4, V5, V6, #V1, #V2, #V3, #V4, #V5, #V6)
#define read7(V1, V2, V3, V4, V5, V6, V7)			get_anys(ifs, V1, V2, V3, V4, V5, V6, V7, #V1, #V2, #V3, #V4, #V5, #V6, #V7)
#define read8(V1, V2, V3, V4, V5, V6, V7, V8) get_anys(ifs, V1, V2, V3, V4, V5, V6, V7, V8, #V1, #V2, #V3, #V4, #V5, #V6, #V7, #V8)


template <typename T> vector<T> make_array(T v1)
{
	vector<T> res(1);
	res[0] = v1;
	return res;
}

template <typename T> vector<T> make_array(T v1, T v2)
{
	vector<T> res(2);
	res[0] = v1;
	res[1] = v2;
	return res;
}

template <typename T> vector<T> make_array(T v1, T v2, T v3)
{
	vector<T> res(3);
	res[0] = v1;
	res[1] = v2;
	res[2] = v3;
	return res;
}

template <typename T> vector<T> make_array(T v1, T v2, T v3, T v4)
{
	vector<T> res(4);
	res[0] = v1;
	res[1] = v2;
	res[2] = v3;
	res[3] = v4;
	return res;
}

template <typename T> vector<T> make_array(T v1, T v2, T v3, T v4, T v5)
{
	vector<T> res(5);
	res[0] = v1;
	res[1] = v2;
	res[2] = v3;
	res[3] = v4;
	res[4] = v5;
	return res;
}

template <typename T> vector<T> make_array(T v1, T v2, T v3, T v4, T v5, T v6)
{
	vector<T> res(6);
	res[0] = v1;
	res[1] = v2;
	res[2] = v3;
	res[3] = v4;
	res[4] = v5;
	res[5] = v6;
	return res;
}


template <typename T> class comb_set
{
public:
	comb_set(int num_of_vars, vector<T> values) {
		init(num_of_vars, values);
	}

	comb_set(int num_of_vars, T v1, T v2) {
		init(num_of_vars, make_array(v1, v2));
	}

	comb_set(int num_of_vars, T v1, T v2, T v3) {
		init(num_of_vars, make_array(v1, v2, v3));
	}

	comb_set(int num_of_vars, T v1, T v2, T v3, T v4) {
		init(num_of_vars, make_array(v1, v2, v3, v4));
	}

	comb_set(int num_of_vars, T v1, T v2, T v3, T v4, T v5) {
		init(num_of_vars, make_array(v1, v2, v3, v4, v5));
	}

	comb_set(int num_of_vars, T v1, T v2, T v3, T v4, T v5, T v6) {
		init(num_of_vars, make_array(v1, v2, v3, v4, v5, v6));
	}

	void next()
	{
		for (int i=0 ; i < num_of_vars ; i++)
		{
			comb[i]++;

			assert(comb[i] >= 0 && comb[i] <= num_of_values_per_var);

			if (comb[i] <  num_of_values_per_var)
				return;

			comb[i] = 0;
		}

		num_of_owerflowns++;
	}

	bool has_wrapped_around()
	{
		return num_of_owerflowns > 0;
	}

	T operator [] (int i)
	{
		return values[comb[i]];
	}

private:

	void init(int nvars, vector<T> vals)
	{
		assert(nvars > 0);

		num_of_vars = nvars;
		num_of_values_per_var = vals.size();
		num_of_owerflowns = 0;
		comb.resize(nvars);
		values = vals;
	}

private:
	int num_of_vars;
	int num_of_values_per_var;
	int num_of_owerflowns;
	int_v comb;
	vector<T> values;
};

int pos_mod(intw n, int d)
{
	int m = n % d;
	if (m < 0)
		m = m + d;
	assert(m >= 0 && m < d);
	return m;
}

template <typename T> class matrix
{
public:
	matrix(int size1, int size2) : v(size1)
	{
		for (int i=0 ; i < size1 ; i++)
			v[i].resize(size2);
	}

	T &operator () (int idx1, int idx2)
	{
		vector<T> &sv = v[idx1];
		T &e = sv[idx2];
		return e;
	}

	int width()
	{
		return v.size();
	}

	int height()
	{
		return v[0].size();
	}

private:
	vector<vector<T>> v;
};

typedef matrix<bool> bool_v2;
typedef matrix<int> int_v2;
typedef matrix<double> double_v2;
typedef matrix<char> char_v2;
typedef matrix<string> str_v2;
typedef matrix<intw> intw_v2;

template <typename T> class ex_vector
{
public:
	ex_vector(int min_idx, int max_idx) : v(max_idx-min_idx+1), min_idx(min_idx), max_idx(max_idx)
	{
		assert(min_idx <= max_idx);
	}

	void set_all(const T &val)
	{
		for (int i=0 ; i < v.size() ; i++)
			v[i] = val;
	}

	T &operator [] (int idx)
	{
		assert(idx >= min_idx && idx <= max_idx);

		return v[idx-min_idx];
	}

public:
	int min_idx;
	int max_idx;

private:
	vector<T> v;
};

template <typename T> class ex_matrix
{
public:
	ex_matrix(int min_idx1, int max_idx1, int min_idx2, int max_idx2) :
			v((max_idx1-min_idx1+1) * (max_idx2-min_idx2+1)),
			min_idx1(min_idx1),	max_idx1(max_idx1),
			min_idx2(min_idx2),	max_idx2(max_idx2)
	{
		assert(min_idx1 <= max_idx1);
		assert(min_idx2 <= max_idx2);
	}

	void set_all(const T &val)
	{
		for (int i=0 ; i < v.size() ; i++)
			v[i] = val;
	}

	T &operator () (int idx1, int idx2)
	{
		assert(idx1 >= min_idx1 && idx1 <= max_idx1);
		assert(idx2 >= min_idx2 && idx2 <= max_idx2);

		int w2 = max_idx2 - min_idx2 + 1;
		int i1 = idx1 - min_idx1;
		int i2 = idx2 - min_idx2;

		int idx = i1 * w2 + i2;

		return v[idx];
	}

public:
	int min_idx1;
	int max_idx1;
	int min_idx2;
	int max_idx2;

private:
	vector<T> v;
};



////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////


const int MAXD = 1005, DIG = 9, BASE = 1000000000;
const unsigned long long BOUND = numeric_limits <unsigned long long> :: max () - (unsigned long long) BASE * BASE;

struct bignum
{
    int D, digits [MAXD / DIG + 2];

    inline void trim ()
    {
        while (D > 1 && digits [D - 1] == 0)
            D--;
    }

    inline void init (long long x)
    {
        memset (digits, 0, sizeof (digits));
        D = 0;

        do
        {
            digits [D++] = x % BASE;
            x /= BASE;
        }
        while (x > 0);
    }

    inline bignum (long long x)
    {
        init (x);
    }

    inline bignum (int x = 0)
    {
        init (x);
    }

    inline bignum (const char *s)
    {
        memset (digits, 0, sizeof (digits));
        int len = strlen (s), first = (len + DIG - 1) % DIG + 1;
        D = (len + DIG - 1) / DIG;

        for (int i = 0; i < first; i++)
            digits [D - 1] = digits [D - 1] * 10 + s [i] - '0';

        for (int i = first, d = D - 2; i < len; i += DIG, d--)
            for (int j = i; j < i + DIG; j++)
                digits [d] = digits [d] * 10 + s [j] - '0';

        trim ();
    }

    inline char *str ()
    {
        trim ();
        char *buf = new char [DIG * D + 1];
        int pos = 0, d = digits [D - 1];

        do
        {
            buf [pos++] = d % 10 + '0';
            d /= 10;
        }
        while (d > 0);

        reverse (buf, buf + pos);

        for (int i = D - 2; i >= 0; i--, pos += DIG)
            for (int j = DIG - 1, t = digits [i]; j >= 0; j--)
            {
                buf [pos + j] = t % 10 + '0';
                t /= 10;
            }

        buf [pos] = '\0';
        return buf;
    }

    inline bool operator < (const bignum &o) const
    {
        if (D != o.D)
            return D < o.D;

        for (int i = D - 1; i >= 0; i--)
            if (digits [i] != o.digits [i])
                return digits [i] < o.digits [i];

        return false;
    }

    inline bool operator == (const bignum &o) const
    {
        if (D != o.D)
            return false;

        for (int i = 0; i < D; i++)
            if (digits [i] != o.digits [i])
                return false;

        return true;
    }

    inline bool operator != (const bignum &o) const
    {
      return !(*this == o);
    }
    
    inline bignum operator << (int p) const
    {
        bignum temp;
        temp.D = D + p;

        for (int i = 0; i < D; i++)
            temp.digits [i + p] = digits [i];

        for (int i = 0; i < p; i++)
            temp.digits [i] = 0;

        return temp;
    }

    inline bignum operator >> (int p) const
    {
        bignum temp;
        temp.D = D - p;

        for (int i = 0; i < D - p; i++)
            temp.digits [i] = digits [i + p];

        for (int i = D - p; i < D; i++)
            temp.digits [i] = 0;

        return temp;
    }

    inline bignum range (int a, int b) const
    {
        bignum temp = 0;
        temp.D = b - a;

        for (int i = 0; i < temp.D; i++)
            temp.digits [i] = digits [i + a];

        return temp;
    }

    inline bignum operator + (const bignum &o) const
    {
        bignum sum = o;
        int carry = 0;

        for (sum.D = 0; sum.D < D || carry > 0; sum.D++)
        {
            sum.digits [sum.D] += (sum.D < D ? digits [sum.D] : 0) + carry;

            if (sum.digits [sum.D] >= BASE)
            {
                sum.digits [sum.D] -= BASE;
                carry = 1;
            }
            else
                carry = 0;
        }

        sum.D = max (sum.D, o.D);
        sum.trim ();
        return sum;
    }

    inline bignum operator - (const bignum &o) const
    {
        bignum diff = *this;

        for (int i = 0, carry = 0; i < o.D || carry > 0; i++)
        {
            diff.digits [i] -= (i < o.D ? o.digits [i] : 0) + carry;

            if (diff.digits [i] < 0)
            {
                diff.digits [i] += BASE;
                carry = 1;
            }
            else
                carry = 0;
        }

        diff.trim ();
        return diff;
    }

    inline bignum operator * (const bignum &o) const
    {
        bignum prod = 0;
        unsigned long long sum = 0, carry = 0;

        for (prod.D = 0; prod.D < D + o.D - 1 || carry > 0; prod.D++)
        {
            sum = carry % BASE;
            carry /= BASE;

            for (int j = max (prod.D - o.D + 1, 0); j <= min (D - 1, prod.D); j++)
            {
                sum += (unsigned long long) digits [j] * o.digits [prod.D - j];

                if (sum >= BOUND)
                {
                    carry += sum / BASE;
                    sum %= BASE;
                }
            }

            carry += sum / BASE;
            prod.digits [prod.D] = sum % BASE;
        }

        prod.trim ();
        return prod;
    }

    inline double double_div (const bignum &o) const
    {
        double val = 0, oval = 0;
        int num = 0, onum = 0;

        for (int i = D - 1; i >= max (D - 3, 0); i--, num++)
            val = val * BASE + digits [i];

        for (int i = o.D - 1; i >= max (o.D - 3, 0); i--, onum++)
            oval = oval * BASE + o.digits [i];

        return val / oval * (D - num > o.D - onum ? BASE : 1);
    }

    inline pair <bignum, bignum> divmod (const bignum &o) const
    {
        bignum quot = 0, rem = *this, temp;

        for (int i = D - o.D; i >= 0; i--)
        {
            temp = rem.range (i, rem.D);
            int div = (int) temp.double_div (o);
            bignum mult = o * div;

            while (div > 0 && temp < mult)
            {
                mult = mult - o;
                div--;
            }

            while (div + 1 < BASE && !(temp < mult + o))
            {
                mult = mult + o;
                div++;
            }

            rem = rem - (o * div << i);

            if (div > 0)
            {
                quot.digits [i] = div;
                quot.D = max (quot.D, i + 1);
            }
        }

        quot.trim ();
        rem.trim ();
        return make_pair (quot, rem);
    }

    inline bignum operator / (const bignum &o) const
    {
        return divmod (o).first;
    }

    inline bignum operator % (const bignum &o) const
    {
        return divmod (o).second;
    }

    inline bignum power (int exp) const
    {
        bignum p = 1, temp = *this;

        while (exp > 0)
        {
            if (exp & 1) p = p * temp;
            if (exp > 1) temp = temp * temp;
            exp >>= 1;
        }

        return p;
    }
};

void to_any(const string &str, bignum &val)
{
	val = bignum(str.c_str());
}

typedef vector<bignum> bignum_v;
