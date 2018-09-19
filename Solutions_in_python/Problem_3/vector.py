import math
class Vec2:
	def __init__(self, x, y, len = None):
		self.x = x
		self.y = y
		self.len = len

	def Len(self):
		if not self.len:
			self.len = self.LenSq()**0.5
		return self.len

	def LenSq(self):
		return self.x**2 + self.y**2

	def Normalize(self):
		l = self.Len()
		self.x /= l
		self.y /= l
		self.len = 1

	def __div__(lhs, rhs):
		return Vec2(lhs.x/rhs, lhs.y/rhs)

	def __mul__(lhs, rhs):
		if isinstance(rhs, Vec2):
			return lhs.x * rhs.x + lhs.y * rhs.y
		return Vec2(rhs * lhs.x, rhs * lhs.y)

	def __xor__(lhs, rhs):
		return lhs.x * rhs.y - lhs.y * rhs.x

	def Rot90(self):
		return Vec2(-self.y, self.x)

	def Rot(self, angle):
		return Vec2(self.x * math.cos(angle) - self.y * math.sin(angle), self.x * math.sin(angle) + self.y * math.cos(angle))

	def __add__(lhs, rhs):
		return Vec2(lhs.x + rhs.x , lhs.y + rhs.y)
	
	def __sub__(lhs, rhs):
		return Vec2(lhs.x - rhs.x , lhs.y - rhs.y)

