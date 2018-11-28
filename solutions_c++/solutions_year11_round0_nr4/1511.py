#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <map>
#include <set>
#include <tr1/unordered_map>
#include <tr1/unordered_set>
#include <stdlib.h>
#include <math.h>

using std::string;
using std::vector;
using std::set;
using std::map;
using std::tr1::unordered_map;
using std::tr1::unordered_set;

static const double MaxSize = 20;

class ProblemSolver {
public:
	ProblemSolver() : ist("input.txt"), ost("output.txt") {}
	void Run();
	void SolveOneTest();

private:
	std::ifstream ist;
	std::ofstream ost;

	vector<vector<double> > m_cnk;
	vector<double> m_facts;
	vector<double> m_answers;

	void calcCnk();
	void precalcFactorials();
	void precalcAnswers();
};

inline void ProblemSolver::calcCnk()
{
	m_cnk = vector<vector<double> >(MaxSize, vector<double>(MaxSize));
	for( int i = 0; i < m_cnk[0].size(); i++ ) {
		m_cnk[0][i] = 1;
	}
	for( int i = 1; i < m_cnk.size(); i++ ) {
		for( int j = i; j < m_cnk[0].size(); j++ ) {
			m_cnk[i][j] = m_cnk[i-1][j-1] + m_cnk[i][j-1];
		}
	}
}

inline void ProblemSolver::Run()
{
	int tn;
	ist >> tn;
//	calcCnk();
//	precalcFactorials();
//	precalcAnswers();
	for( int i = 0; i < tn; i++ ) {
		ost << "Case #" << (i+1) << ": ";
		SolveOneTest();
	}
}

inline void ProblemSolver::precalcFactorials()
{
	m_facts.resize(MaxSize);
	m_facts[0] = 1;
	for( int i = 1; i < m_facts.size(); i++ ) {
		m_facts[i] = m_facts[i-1] * i;
	}
}

inline void ProblemSolver::precalcAnswers()
{
	vector<double> permProbs(MaxSize);
	m_answers.resize(MaxSize);
	m_answers[0] = 0;
	m_answers[1] = 0;
	permProbs[0] = 0;
	permProbs[1] = 0;
	for( int i = 2; i < MaxSize; i++ ) {
		m_answers[i] = 1.0 * i / (i - 1);
		for( int j = 1; j < i; j++ ) {
			m_answers[i] += (m_answers[j] + permProbs[i - j])
				* m_cnk[j-1][i-1] * m_facts[j - 1] * m_facts[i - j] / (m_facts[i - 1] * (i - 1));
			permProbs[i] += (m_answers[j] + permProbs[i - j])
				* m_cnk[j-1][i-1] * m_facts[j - 1] * m_facts[i - j] / (m_facts[i]);
		}
		permProbs[i] += m_answers[i] / i;
		std::cerr << i << "=" << m_answers[i] << " permProbs=" << permProbs[i] << std::endl;
	}
}

inline void ProblemSolver::SolveOneTest() 
{
	int n;
	ist >> n;
	std::vector<int> a(n);
	double res = 0;
	for( int i = 0; i < n; i++ ) {
		ist >> a[i];
		if( a[i] - 1 != i ) {
			res = res + 1;
		}
	}
	ost << res << "\n";
}

int main() 
{
	ProblemSolver solver;
	solver.Run();
	return 0;
}
