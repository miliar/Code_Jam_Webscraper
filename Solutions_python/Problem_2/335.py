class Schedule():
	def __init__(self, departure,arrival):
		self._dep =departure.split(':')
		self._arr = arrival.split(':')
		
	def __cmp__(self, other):
		_hour = int(self._dep[0])
		_ohour = int(other._dep[0])
		_min = int(self._dep[1])
		_omin = int(other._dep[1])
		if(_hour < _ohour):
			return -1
		elif(_hour == _ohour and _min < _omin):
			return -1
		else:
			return 1

		
	def validDeparture(self,dep_hour,dep_min,turnaround):
		_time = []
		_hour = int(self._arr[0])
		_min = int(self._arr[1])
		_min = _min + turnaround;
		if(_min > 60):
			_hour = _hour + 1
			_min = _min-60
		if(dep_hour > _hour):
			return True
		elif(dep_hour == _hour and dep_min >= _min):
			return True
		else:
			return False