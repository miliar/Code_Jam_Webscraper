#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

class Time {
public:
	int hour_;
	int min_;

	bool operator <= (Time &other)
	{
		if (hour_ < other.hour_)
			return true;

		if (hour_ == other.hour_ && min_ <= other.min_)
			return true;

		return false;
	}

	Time operator + (int min)
	{
		Time time(*this);

		time.min_ += min;
		if (time.min_ >= 60) {
			time.hour_++;
			time.min_ -= 60;
		}

		return time;
	}

	Time& operator = (const Time &other)
	{
		hour_ = other.hour_;
		min_ = other.min_;

		return *this;
	}
};

enum {
	PART_A = 1,
	PART_B = 2
};

class Train
{
	friend class Solution;

public:
	bool operator < (Train &other)
	{
		if (start_.hour_ < other.start_.hour_)
			return true;

		if (start_.hour_ == other.start_.hour_ &&
			start_.min_ < other.start_.min_)
			return true;

		return false;
	}

	void Parse(string start, string arrive, int part)
	{
		string hour,min;
		
		hour = start.substr(0, 2);
		min = start.substr(3, 2);

		start_.hour_ = atoi(hour.c_str());
		start_.min_ = atoi(min.c_str());

		hour = arrive.substr(0, 2);
		min = arrive.substr(3, 2);

		arrive_.hour_ = atoi(hour.c_str());
		arrive_.min_ = atoi(min.c_str());

		belong_ = part;
		ignore_ = false;
		need_ = true;
	}

private:
	Time	start_;
	Time	arrive_;
	int		belong_;
	bool	need_;
	bool	ignore_;
};

class Solution
{
public:
	void Input()
	{
		int atobNum, btoaNum;
		string start, end;
		Train train;

		trains_.clear();

		cin >> turnaround_;

		cin >> atobNum >> btoaNum;

		for (int i = 0; i < atobNum; ++i) {
			cin >> start >> end;
			
			train.Parse(start, end, PART_A);
			trains_.push_back(train);
		}

		for (int i = 0; i < btoaNum; ++i) {
			cin >> start >> end;

			train.Parse(start, end, PART_B);
			trains_.push_back(train);
		}

		sort(trains_.begin(), trains_.end());

	}
	
	void BackTracking(Train train, int region)
	{
	}

	void Process()
	{
		int i, j, from;
		int count = 0, maxSeq;
		Train train1, train2;
		Time time;

		while (true) {
			maxSeq = 0;

			table_.resize(0);
			table_.resize(trains_.size(), 0);
			backtrace_.resize(0);
			backtrace_.resize(trains_.size(), -1);

			for (i = 1; i < trains_.size(); ++i) {
				count = 0;
				train1 = trains_[i];

				if (train1.ignore_ == true) continue;

				count = -1;
				from = 0;

				for (j = 0; j < i; ++j) {
					train2 = trains_[j];

					if (train2.ignore_) continue;

					time = train2.arrive_;
					time = time + turnaround_;

					if (train1.belong_ != train2.belong_ && time <= train1.start_) {
						if (table_[j] + 1 > count) {
							count = table_[j] + 1;
							from = j;
						}
					}
				}

				if (count != -1) {
					table_[i] = count;
					backtrace_[i] = from;
				}	
			}

			for (i = 0; i < table_.size(); ++i) {
				if (table_[i] > maxSeq) {
					maxSeq = table_[i];
					from = i;
				}
			}

			if (maxSeq == 0) break;

			do {
				trains_[from].ignore_ = true;
				trains_[from].need_ = false;
				from = backtrace_[from];
			} while (backtrace_[from] != -1);
			trains_[from].ignore_ = true;
		}
	}

	void Output()
	{
		int i, countA = 0, countB = 0;

		for (i = 0; i < trains_.size(); ++i) {
			if (trains_[i].need_ == true) {
				switch (trains_[i].belong_) {
					case PART_A:
						countA++;
						break;
					case PART_B:
						countB++;
						break;
				}
			}
		}

		cout << countA << " " << countB << endl;
	}

private:
	int turnaround_;
	vector<Train> trains_;
	vector<int> backtrace_;
	vector<int> table_;
};


int main()
{
	int testcase;
	Solution sol;

	cin >> testcase;

	for (int i = 0; i < testcase; ++i) {
		sol.Input();
		sol.Process();
		cout << "Case #" << i + 1 << ": ";
		sol.Output();
	}

	return 0;
}
